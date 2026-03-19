from collections import deque
from datetime import datetime, timezone
import os
import threading

from flask import Flask, jsonify, request
import serial

app = Flask(__name__)

SERIAL_PORT = os.getenv("SERIAL_PORT", "COM3")
SERIAL_BAUD = int(os.getenv("SERIAL_BAUD", "9600"))
MAX_EVENTS = 120

state_lock = threading.Lock()

data = {
    "status": "Idle",
    "waste": "None",
    "source": "simulated",
    "serial_connected": False,
    "updated_at": datetime.now(timezone.utc).isoformat()
}

stats = {
    "wet_count": 0,
    "dry_count": 0,
    "detection_count": 0
}

events = deque(maxlen=MAX_EVENTS)


def iso_now():
    return datetime.now(timezone.utc).isoformat()


def add_event(message):
    events.appendleft({"time": iso_now(), "message": message})


def update_state(status=None, waste=None, source=None):
    with state_lock:
        previous_status = data["status"]
        previous_waste = data["waste"]

        if status is not None:
            data["status"] = status
        if waste is not None:
            data["waste"] = waste
        if source is not None:
            data["source"] = source

        data["updated_at"] = iso_now()

        if data["status"] == "Object Detected" and previous_status != "Object Detected":
            stats["detection_count"] += 1
        if data["waste"] == "Wet Waste" and previous_waste != "Wet Waste":
            stats["wet_count"] += 1
        if data["waste"] == "Dry Waste" and previous_waste != "Dry Waste":
            stats["dry_count"] += 1


def initialize_serial():
    try:
        conn = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)
        data["serial_connected"] = True
        data["source"] = "hardware"
        add_event("Serial connected on " + SERIAL_PORT)
        return conn
    except Exception as exc:
        data["serial_connected"] = False
        data["source"] = "simulated"
        add_event("Serial unavailable on " + SERIAL_PORT + ": " + str(exc))
        return None


ser = initialize_serial()


def map_serial_line(line):
    if line == "DETECTED":
        update_state(status="Object Detected", source="hardware")
        add_event("Object detected")
    elif line == "WET":
        update_state(waste="Wet Waste", source="hardware")
        add_event("Classified as wet waste")
    elif line == "DRY":
        update_state(waste="Dry Waste", source="hardware")
        add_event("Classified as dry waste")
    elif line == "IDLE":
        update_state(status="Waiting", source="hardware")
        add_event("System waiting")


def read_serial():
    if ser is None:
        return
    while True:
        try:
            line = ser.readline().decode(errors="ignore").strip().upper()
            if line:
                map_serial_line(line)
        except Exception:
            with state_lock:
                data["serial_connected"] = False
                data["source"] = "simulated"
                data["updated_at"] = iso_now()
            add_event("Serial read error. Backend switched to simulated mode.")
            break


if ser is not None:
    thread = threading.Thread(target=read_serial, daemon=True)
    thread.start()


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    return response


@app.route("/")
def home():
    return jsonify({
        "service": "Urban Waste Backend",
        "status": "running",
        "serial_port": SERIAL_PORT,
        "serial_connected": data["serial_connected"]
    })


@app.route("/health")
def health():
    return jsonify({"ok": True, "time": iso_now(), "serial_connected": data["serial_connected"]})


@app.route("/data")
def get_data():
    with state_lock:
        payload = dict(data)
        payload["stats"] = dict(stats)
    return jsonify(payload)


@app.route("/stats")
def get_stats():
    with state_lock:
        payload = dict(stats)
        payload["source"] = data["source"]
        payload["updated_at"] = data["updated_at"]
    return jsonify(payload)


@app.route("/events")
def get_events():
    limit = request.args.get("limit", default=20, type=int)
    if limit < 1:
        limit = 1
    if limit > MAX_EVENTS:
        limit = MAX_EVENTS
    return jsonify({"events": list(events)[:limit]})


@app.route("/simulate", methods=["POST"])
def simulate_update():
    body = request.get_json(silent=True) or {}
    status = body.get("status")
    waste = body.get("waste")

    if status is None and waste is None:
        return jsonify({"error": "Provide status and/or waste"}), 400

    update_state(status=status, waste=waste, source="simulated")
    add_event("Manual simulate update")
    return get_data()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
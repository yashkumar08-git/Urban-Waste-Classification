from flask import Flask, jsonify
import serial
import threading

app = Flask(__name__)

# Update COM port (IMPORTANT)
try:
    ser = serial.Serial('COM3', 9600, timeout=1)
except Exception:
    ser = None

data = {
    "status": "Idle",
    "waste": "None"
}

def read_serial():
    global data
    if ser is None:
        return
    while True:
        try:
            line = ser.readline().decode().strip()

            if line == "DETECTED":
                data["status"] = "Object Detected"

            elif line == "WET":
                data["waste"] = "Wet Waste"

            elif line == "DRY":
                data["waste"] = "Dry Waste"

            elif line == "IDLE":
                data["status"] = "Waiting"

        except:
            pass

# Run serial reading in background only when serial is available
if ser is not None:
    thread = threading.Thread(target=read_serial)
    thread.daemon = True
    thread.start()

@app.route('/data')
def get_data():
    return jsonify(data)

@app.route('/')
def home():
    return "Backend Running"

if __name__ == "__main__":
    app.run(debug=True)
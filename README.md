# Urban Waste Classification – Intelligent IoT Based System

## Introduction

Urban waste management is a major challenge in modern cities. Improper waste segregation leads to pollution and inefficient recycling.
This project presents an **IoT-based intelligent waste classification system** that automatically detects and segregates waste into wet and dry categories using sensors, microcontrollers, and a real-time dashboard.

---

## Problem Statement

In urban environments, waste is often disposed of without proper segregation. Manual sorting is inefficient, time-consuming, and error-prone.
An automated smart system is required to improve waste management and sustainability.

---

## Objectives

* Automate waste segregation using IoT sensors
* Detect waste using IR sensor
* Identify wet and dry waste using rain sensor
* Control bin lid using servo motor
* Redirect waste using stepper motor
* Display real-time system data on dashboard

---

## Hardware Components

* Arduino Uno
* Servo Motor
* IR Sensor
* Rain Sensor
* Stepper Motor
* Stepper Motor Driver (ULN2003)
* Jumper Wires

---

## Software & Technologies

* Arduino IDE
* Python (Flask Backend)
* HTML, CSS, JavaScript (Frontend Dashboard)
* Git & GitHub

---

## System Architecture

```id="l0z1j1"
Arduino → Serial Communication → Flask Backend → REST API → Frontend Dashboard
```

---

## System Workflow

1. User approaches the smart waste bin
2. IR sensor detects waste
3. Servo motor opens lid automatically
4. Rain sensor detects moisture level
5. System classifies waste as wet or dry
6. Stepper motor directs waste into correct compartment
7. Backend receives data from Arduino
8. Frontend dashboard displays real-time system status

---

## Features

* Real-time waste detection
* Automatic classification (Wet/Dry)
* Motor-based waste redirection
* Live dashboard with system status
* Event tracking and statistics
* Backend API for data communication

---

## Project Progress

### Week 1 – Component Testing

* Hardware components tested individually
* Servo motor, IR sensor, rain sensor, stepper motor tested
* Repository and folder structure created

### Week 2 – System Integration

* Sensors integrated with Arduino
* Wet/dry detection logic implemented
* Stepper motor direction control added
* Full system logic developed

### Week 3 – Final System & Dashboard

* Complete hardware assembly
* Backend developed using Flask
* Real-time dashboard created
* Arduino integrated with backend
* System debugging and testing completed

---

## Project Structure

```id="u08gbk"
Urban-Waste-Classification
│
├── docs
├── hardware
│   └── arduino
├── backend
│   └── app.py
├── frontend
│   └── index.html
├── diagrams
├── requirements.txt
├── README.md
└── TEAM-CONTRIBUTION.md
```

---

## How to Run the Project

### 1. Upload Arduino Code

* Connect Arduino to system
* Upload the final Arduino program

### 2. Run Backend

```id="k2xxn1"
cd backend
python app.py
```

### 3. Run Frontend

* Open `frontend/index.html` using Live Server

### 4. View Dashboard

```id="b4k2zn"
http://127.0.0.1:5500
```

---

## Current Status

The system is fully functional with real-time data flow from Arduino to dashboard.
The project is ready for demonstration and evaluation.

---

## Team Members

### Samarth Gupta – Project Leader & Hardware Integration

Responsible for hardware setup, wiring, and system architecture.

### Yash Kumar – Arduino & Backend Development

Responsible for Arduino programming, backend development, and system integration.

### Prince Raikwar – Documentation & Frontend Development

Responsible for documentation, system explanation, and dashboard UI.

---

## Conclusion

This project demonstrates how IoT technology can be used to build an intelligent waste management system that improves efficiency, reduces manual effort, and promotes environmental sustainability.

---

## Future Scope

* AI-based waste classification using camera
* Mobile app integration
* Cloud-based monitoring system
* Smart city integration

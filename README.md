# Urban Waste Classification – Intelligent IoT Based System

## Introduction

Urban waste management is a major environmental challenge in modern cities. Improper waste segregation leads to inefficient recycling and environmental pollution.
This project aims to develop an **IoT-based intelligent waste classification system** that automatically detects and separates waste using sensors and motor-driven mechanisms.

---

## Problem Statement

Manual waste segregation is inefficient and time-consuming. There is a need for an automated system that can identify different types of waste and direct them into appropriate compartments.

---

## Objectives

* Automate waste segregation using IoT sensors.
* Detect waste insertion using proximity/IR sensors.
* Identify wet and dry waste using a rain sensor.
* Control lid opening using a servo motor.
* Redirect waste using a stepper motor mechanism.
* Build a smart and sustainable waste management prototype.

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

## Software Tools

* Arduino IDE
* VS Code
* Git & GitHub

---

## System Workflow

1. User approaches the smart waste bin.
2. IR sensor detects waste insertion.
3. Servo motor opens the bin lid automatically.
4. Rain sensor checks moisture level of waste.
5. System determines whether the waste is **wet or dry**.
6. Stepper motor rotates the compartment to direct waste to the correct section.

---

## Project Progress

### Week 1 – Component Testing

* Repository and folder structure created
* Servo motor testing completed
* IR sensor testing completed
* Rain sensor testing completed
* Stepper motor testing completed

### Week 2 – System Integration

* IR sensor integrated with servo motor
* Rain sensor wet/dry detection logic implemented
* Stepper motor direction control implemented
* Sensor combination logic developed
* Full system integration code created

### Week 3 – Hardware Assembly

* Final hardware assembly of components
* Sensor placement and hardware layout design
* Wiring verification and stability testing

---

## Team Members

### Samarth Gupta – Project Leader & Hardware Integration

Responsible for hardware assembly, wiring verification, and system architecture design.

### Yash Kumar – Arduino Programming & System Integration

Responsible for writing Arduino code, integrating sensors and motors, and developing system logic.

### Prince Raikwar – Documentation & Backend Development

Responsible for project documentation, report preparation, and backend/dashboard development.

---

## Current Status

Hardware integration and system testing are in progress.
Next phase includes system optimization and project demonstration.

---

## Repository Structure

```
Urban-Waste-Classification
│
├── docs
├── hardware
│   └── arduino
├── backend
├── frontend
├── diagrams
├── README.md
└── TEAM-CONTRIBUTION.md
```

---

## Conclusion

This project demonstrates the use of IoT technology to create an intelligent waste management system that improves urban sustainability and promotes efficient recycling.
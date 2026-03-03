# IR Sensor Testing

## Objective
To test the IR (Infrared) sensor for detecting object presence in front of the smart waste bin.

---

## Components Used
- Arduino Uno
- IR Obstacle Sensor Module
- Jumper Wires

---

## Connection Details

| IR Sensor Pin | Arduino Pin |
|--------------|------------|
| VCC          | 5V         |
| GND          | GND        |
| OUT          | Pin 2      |

---

## Working Principle
The IR sensor emits infrared light.  
When an object comes in front of the sensor, the reflected IR light is detected.

- If object detected → Output becomes LOW  
- If no object → Output remains HIGH  

---

## Arduino Logic
- The IR sensor output is connected to digital pin 2.
- Arduino reads the sensor value using `digitalRead()`.
- If value is LOW → Print "Object Detected!"
- Else → Print "No Object"

---

## Code Behavior
When the program runs:
- Serial Monitor displays detection status.
- Baud rate used: 9600.

---

## Result
The IR sensor successfully detects object presence.  
Object detection message appears correctly in Serial Monitor.

---

## Conclusion
IR sensor testing is successful and ready for integration with servo motor logic in the next phase.
# Rain Sensor Testing

## Objective
To test the rain sensor module for detecting wet and dry conditions in the smart waste segregation system.

---

## Components Used
- Arduino Uno
- Rain Drop Sensor Module
- Jumper Wires

---

## Connection Details

| Rain Sensor Pin | Arduino Pin |
|----------------|------------|
| VCC            | 5V         |
| GND            | GND        |
| AO (Analog Out)| A0         |

---

## Working Principle
The rain sensor detects moisture on its surface.

- When dry → Higher analog value
- When wet → Lower analog value

The Arduino reads the sensor value using `analogRead()`.

---

## Arduino Logic
- Sensor connected to analog pin A0.
- Arduino continuously reads sensor value.
- If value < 500 → Wet Waste Detected
- If value >= 500 → Dry Waste Detected

(Note: Threshold value may vary depending on environment.)

---

## Code Behavior
- Serial Monitor displays sensor value.
- Wet/Dry condition is printed every second.
- Baud rate used: 9600.

---

## Observations
- Dry sensor value: (Write your observed value here)
- Wet sensor value: (Write your observed value here)

---

## Result
Rain sensor successfully detects wet and dry conditions.

---

## Conclusion
Rain sensor testing is successful and ready for integration with servo and IR sensor logic for complete waste classification.
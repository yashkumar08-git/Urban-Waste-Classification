# Stepper Motor Testing

## Objective
To test the stepper motor for rotational control in the smart waste segregation system.

---

## Components Used
- Arduino Uno
- Stepper Motor
- Stepper Motor Driver Module
- Jumper Wires

---

## Connection Details

| ULN2003 Pin | Arduino Pin |
|------------|------------|
| IN1        | 8          |
| IN2        | 9          |
| IN3        | 10         |
| IN4        | 11         |
| VCC        | 5V         |
| GND        | GND        |

The stepper motor is connected directly to the ULN2003 driver board.

---

## Working Principle
A stepper motor rotates in small steps instead of continuous rotation.

- One full rotation = 2048 steps (for 28BYJ-48 motor)
- Direction can be controlled (clockwise / counterclockwise)

Arduino controls the motor using the Stepper library.

---

## Arduino Logic
- Stepper library initialized with 2048 steps per revolution.
- Motor speed set using `setSpeed()`.
- Motor rotates one full revolution clockwise.
- Then rotates one full revolution counterclockwise.

---

## Code Behavior
- Serial Monitor prints rotation direction.
- Motor rotates forward and backward repeatedly.
- Rotation delay used for clear observation.

---

## Observations
- Motor rotates smoothly in both directions.
- Speed is stable at 10 RPM.
- No overheating observed during short testing.

---

## Result
Stepper motor successfully tested and working properly.

---

## Conclusion
Stepper motor is ready for integration with waste classification logic for directing waste into separate compartments.
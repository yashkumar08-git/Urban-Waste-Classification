#include <Stepper.h>

const int stepsPerRevolution = 2048;

Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
  Serial.begin(9600);
  myStepper.setSpeed(10);
}

void loop() {
  Serial.println("Clockwise Rotation");
  myStepper.step(stepsPerRevolution);

  delay(2000);

  Serial.println("Counter Clockwise Rotation");
  myStepper.step(-stepsPerRevolution);

  delay(2000);
}
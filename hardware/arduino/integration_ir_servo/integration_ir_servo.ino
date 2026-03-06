#include <Servo.h>

Servo myServo;
int irPin = 2;

void setup() {
  pinMode(irPin, INPUT);
  myServo.attach(9);
  myServo.write(0);   // Lid closed
  Serial.begin(9600);
}

void loop() {
  int sensorValue = digitalRead(irPin);

  if (sensorValue == LOW) {
    Serial.println("Object detected - Opening lid");

    myServo.write(90);   // Open lid
    delay(3000);

    myServo.write(0);    // Close lid
    Serial.println("Lid closed");
  }

  delay(500);
}
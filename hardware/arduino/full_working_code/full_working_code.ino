#include <Servo.h>

#define trigPin 7
#define echoPin 8
#define rainPin A0
#define servoPin 6

Servo myServo;

void setup() {
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  myServo.attach(servoPin);
  myServo.write(90); // Center position
}

void loop() {

  long duration;
  float distance;

  // ===== ULTRASONIC =====
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH, 30000);

  if (duration == 0) {
    Serial.println("No object detected");
    myServo.write(70);
    delay(500);
    return;
  }

  distance = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // ===== OBJECT DETECTED =====
  if (distance < 15) {

    Serial.println("Object detected! Waiting 6 sec...");
    delay(6000);

    int rainValue = analogRead(rainPin);

    Serial.print("Rain Value: ");
    Serial.println(rainValue);

    // ===== CLASSIFICATION =====
    if (rainValue < 500) {
      // WET WASTE
      Serial.println("WET → RIGHT");
      myServo.write(125);
    } 
    else {
      // DRY WASTE (default)
      Serial.println("DRY → LEFT");
      myServo.write(20);
    }

    delay(3000);  // Hold position

    // Return to center
    myServo.write(70);
  } 
  else {
    // No object
    myServo.write(70);
  }

  delay(500);
}
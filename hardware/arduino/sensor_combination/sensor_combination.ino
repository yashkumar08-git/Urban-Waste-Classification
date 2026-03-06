#include <Servo.h>

Servo myServo;

int irPin = 2;
int rainPin = A0;

void setup() {
  pinMode(irPin, INPUT);
  myServo.attach(9);
  Serial.begin(9600);
}

void loop() {

  int irValue = digitalRead(irPin);

  if(irValue == LOW){

    Serial.println("Waste detected");

    myServo.write(90);
    delay(2000);

    int rainValue = analogRead(rainPin);

    if(rainValue < 500){
      Serial.println("Wet Waste");
    }
    else{
      Serial.println("Dry Waste");
    }

    myServo.write(0);
  }

  delay(1000);
}
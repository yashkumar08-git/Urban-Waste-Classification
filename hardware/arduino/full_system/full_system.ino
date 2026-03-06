#include <Servo.h>
#include <Stepper.h>

Servo myServo;

const int stepsPerRevolution = 2048;

Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);

int irPin = 2;
int rainPin = A0;

void setup() {

  pinMode(irPin, INPUT);
  myServo.attach(6);

  Serial.begin(9600);

  myStepper.setSpeed(10);

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

      myStepper.step(stepsPerRevolution);

    }
    else{

      Serial.println("Dry Waste");

      myStepper.step(-stepsPerRevolution);

    }

    delay(2000);

    myServo.write(0);

  }

  delay(1000);

}
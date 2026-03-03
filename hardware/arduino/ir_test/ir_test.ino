int irPin = 2;

void setup() {
  pinMode(irPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = digitalRead(irPin);

  if (sensorValue == LOW) {
    Serial.println("Object Detected!");
  } else {
    Serial.println("No Object");
  }

  delay(500);
}
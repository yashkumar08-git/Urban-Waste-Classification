int rainPin = A0;
int sensorValue = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(rainPin);

  Serial.print("Rain Sensor Value: ");
  Serial.println(sensorValue);

  if(sensorValue < 500){
    Serial.println("Wet Waste Detected");
  }
  else{
    Serial.println("Dry Waste Detected");
  }

  delay(1000);
}
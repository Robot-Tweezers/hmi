#include <Arduino.h>
//#include <HardwareSerial.h>
//#include <WiFi.h>


void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char dat = Serial.read();
    Serial.write(dat);
    Serial.write(dat);
  }
}

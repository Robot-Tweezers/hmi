//#include <Arduino.h>

int potPin = A0;
int buttonPin = A1;

int potvalue;
int buttonvalue;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT);
}

void loop() {
  potvalue = analogRead(potPin);
  buttonvalue = digitalRead(buttonPin);

  Serial.print("p");
  Serial.println(potvalue);
  Serial.print("b");
  Serial.println(buttonvalue);
}

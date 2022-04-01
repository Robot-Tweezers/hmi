#include <Arduino.h>
#include <HardwareSerial.h>

#include <pb_encode.h>
#include <pb_decode.h>

#include "remote.pb.h"

#include "cobs.h"

HardwareSerial s1 = HardwareSerial(1);
COBEncoder enc = COBEncoder(s1);

void setup() {
	s1.begin(9600, SERIAL_8N1, GPIO_NUM_16, GPIO_NUM_17); // For loopback
}




void loop() {

}
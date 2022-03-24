// #include <Arduino.h>
// #include <HardwareSerial.h>
// #include <WiFi.h>

// #include <stdlib.h>

// #include <pb_encode.h>
// #include <pb_decode.h>

// #include "remote.pb.h"

// #define LED 0

// int i;

// uint8_t inbuffer[128];
// uint8_t outbuffer[128];
// bool status;
// int message_length;

// WiFiServer wifiServer(80);

// void initWiFi() {
//   WiFi.mode(WIFI_STA);
//   WiFi.begin("BurstYe", "RawTrut5ch");
//   Serial.print("Connecting to WiFi ..");
//   while (WiFi.status() != WL_CONNECTED) {
//     Serial.print('.');
//     delay(1000);
//   }
//   Serial.println(WiFi.localIP());
//   wifiServer.begin();
// }


// void protobuf_test_loop() {

// 	int sensorValue = analogRead(A0);
// 	printf("Sensor value: %d\n", sensorValue);

// 	RemoteData d = RemoteData_init_zero;

// 	pb_ostream_t stream = pb_ostream_from_buffer(inbuffer+1, sizeof(inbuffer)-1);

// 	d.roll = 1.234;
// 	d.pitch = 2.468;
// 	d.x = 1.0001;

// 	status = pb_encode(&stream, RemoteData_fields, &d);
// 	message_length = stream.bytes_written;
// 	outbuffer[0] = message_length;

// 	printf("%d bytes written\n", message_length);

// 	if (!status) {
// 		Serial.write("Encoding failed: ");
// 		Serial.println(PB_GET_ERROR(&stream));
// 		return;
// 	}

// 	// Copy inbuffer to outbuffer
// 	memcpy(outbuffer, inbuffer, 64);

// 	RemoteData d2 = RemoteData_init_zero;
// 	pb_istream_t istream = pb_istream_from_buffer(outbuffer+1, outbuffer[0]);
// 	status = pb_decode(&istream, RemoteData_fields, &d2);

// 	if (!status) {
// 		printf("Decoding Failed: %s\n", PB_GET_ERROR(&istream));
// 		return;
// 	}

// 	Serial.println("Data:");
// 	Serial.write("Roll: ");
// 	Serial.println(d.roll);

// 	delay(500);
// 	Serial.write("\nHello, world ");
// 	Serial.println(i++);
// }


// void wifi_loop() {
// 	WiFiClient client = wifiServer.available();

// 	int size;

// 	if (client) {
// 		while (client.connected()) {

// 			size = client.available();

// 			if (size > 0) {
// 				client.readBytes(inbuffer, sizeof(inbuffer));
// 				Serial.println(size);

// 				client.write(inbuffer, sizeof(inbuffer));
// 			}

// 			delay(10);
// 		}

// 		client.stop();
// 		Serial.println("Client disconnected");
// 	}

// 	Serial.print("Waiting for client... IP address: ");
// 	Serial.println(WiFi.localIP());
// 	delay(1000);
// }

// HardwareSerial s1 = HardwareSerial(1);
// // HardwareSerial s2 = HardwareSerial(2);


// void setup() {

// 	Serial.begin(9600);

// 	// pinMode(GPIO_NUM_9, INPUT_PULLUP);

// 	// i = 0;

// 	s1.begin(9600, SERIAL_8N1, GPIO_NUM_16, GPIO_NUM_17); // For loopback
// 	// s2.begin(9600, SERIAL_8N1, 27, 28);

// 	delay(1000);
// 	// initWiFi();
// }



// void loop() {

// 	// Serial.println("Hello, world!");

// 	// if (digitalRead(GPIO_NUM_9)) {
// 	// 	Serial.println("High");
// 	// } else {
// 	// 	Serial.println("low");
// 	// }

// 	if (Serial.available()) {
// 		char dat = Serial.read();
// 		s1.write(dat);
// 	}

// 	if (s1.available()) {
// 		Serial.write(s1.read());
// 	}
// }
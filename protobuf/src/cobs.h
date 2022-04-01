#ifndef COBS_H
#define COBS_H

#include <stdlib.h>
#include <HardwareSerial.h>

class COBEncoder {
		HardwareSerial s;
		int buffsize;

		char buff[256];
		int bufpos;
		bool clear;
		int next0;

	public:
		COBEncoder(HardwareSerial serial);
		void write(char *byte, int len);
		void reset();
		bool decode(char byte);
		int available(char *msg);

};

#endif /* COBS_H */
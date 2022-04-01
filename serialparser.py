from time import sleep
import serial

# Parses data from an ardunio serial bus which gives the potentiometer & switch data
class Serialparser:
	def __init__(self, serialdevice, baudrate):
		self.serialdevice = serialdevice
		self.baudrate = baudrate

		self.ser = serial.Serial(serialdevice, baudrate)

		self.available = True
		self.switch = 0
		self.pot = 0

		self.newpot = 0
		self.newswitch = 0

	def msg_available(self):
		while self.ser.in_waiting > 4:
			dat = self.ser.readline()
			if dat:
				try:
					ds = dat.decode("utf8")
				except ValueError:
					return

				if ds[0] == 'b':
					self.switch = int(ds[1])
					self.newswitch = True
				elif ds[0] == 'p':
					self.pot = int(ds[1:])
					self.newpot = True

			# dat = self.ser.readline()

		return self.newswitch and self.newpot

	def getmsg(self):
		self.newswitch = False
		self.newpot = False
		return (self.pot, self.switch)


if __name__ == "__main__":
	s = Serialparser("/dev/cu.usbmodem14101", 9600)

	while True:
		if s.msg_available():
			(pot, switch) = s.getmsg()
			print(pot)
			# print(f"Pot: {pot:04d}, Switch: {switch}")
		else:
			pass

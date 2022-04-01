from tkinter import Y
from xmlrpc.client import ProtocolError

from serialparser import Serialparser
from time import sleep

class HMIServer:
	def __init__(self, port, host, vive, serialparser):
		self.port = port
		self.host = host
		self.vive = vive
		self.serialparser = serialparser

		self.pot_position = 0
		self.en_switch = 0

		self.gain = 0

		self.X = 0
		self.Y = 0
		self.Z = 0
		self.Roll = 0
		self.Pitch = 0
		self.Yaw = 0

	def update_data(self):
		# Get data from arduino over serial (potentiometer and limit switch)
		if self.serialparser != None and self.serialparser.msg_available():
			(self.pot_position, self.en_switch) = self.serialparser.getmsg()
			# print(self.pot_position)

		# Get the data from GUI

		# Get data from the vive


	def send_data(self):
		pass

	def start(self):
		while True:
			self.update_data()
			self.send_data()
			print(f"Gain: {self.gain}")
			sleep(0.5)

if __name__ == "__main__":
	s = Serialparser("/dev/cu.usbmodem14101", 9600)
	hmis = HMIServer(0, 0, 0, s)
	hmis.start()

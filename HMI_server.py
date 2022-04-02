from tkinter import Y
from xmlrpc.client import ProtocolError

from serialparser import Serialparser
from time import sleep

import orientation_msg_pb2

import socket

class HMIServer:
	def __init__(self, host, port, vive, serialparser):
		self.port = port
		self.host = host

		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.s.settimeout(1) # seconds
			self.s.connect((self.host, self.port))
		except socket.error:
			print("!!!! Socket error! Not connected to client !!!!")

		self.vive = vive
		self.serialparser = serialparser

		self.pot_position = 0
		self.en_switch = 0

		self.gain = 0

		self.x = 0
		self.y = 0
		self.z = 0
		self.roll = 0
		self.pitch = 0
		self.yaw = 0

	def update_data(self):
		# Get data from arduino over serial (potentiometer and limit switch)
		if self.serialparser != None and self.serialparser.msg_available():
			(self.pot_position, self.en_switch) = self.serialparser.getmsg()
			# print(self.pot_position)

		# Data from the GUI is pushed from the gui thread.

		# Get data from the vive

	def send_data(self):
		d = orientation_msg_pb2.OrientationMsg()
		d.roll = 1.34
		d.pitch = 13.45
		d.yaw = 15.62

		print("Sending Data: ", d)

		dbytes = d.SerializeToString()

		self.s.sendall(dbytes)

		try:
			print(self.s.recv(1024))
		except socket.timeout:
			pass



	def start(self):
		while True:
			self.update_data()
			self.send_data()
			sleep(0.5)

if __name__ == "__main__":
	s = Serialparser("/dev/cu.usbmodem14101", 9600)
	hmis = HMIServer(0, 0, 0, s)
	hmis.start()

import socket
import remote_pb2
import time
import random

from google.protobuf import message

class Teensy:
    def __init__(self, port, host=socket.gethostname()):
        self.port = port
        self.host = host


        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.host, self.port))
        except socket.error:
            pass

    def sendRemoteData(self, x, y, z, roll, pitch, yaw, gripAngle):
        d = remote_pb2.RemoteData()
        d.x = x
        d.y = y
        d.z = z
        d.roll = roll
        d.pitch = pitch
        d.yaw = yaw
        d.gripAngle = gripAngle

        ds = d.SerializeToString()



        resp = self.sendBytes(d.SerializeToString())

        try:
            d2 = remote_pb2.RemoteData()
            d2.ParseFromString(resp)
            print(d2)
        except message.DecodeError:
            print(resp)

    def sendBytes(self, dat):
        self.s.sendall(dat)
        return self.s.recv(1024)

    def close(self):
        self.s.close()

    def test_serialize():
        d = remote_pb2.RemoteData()
        d.x = 1
        d.y = 2
        d.z = 3
        d.roll = 4
        d.pitch = 5
        d.yaw = 6.321
        d.gripAngle = -0.000135

        d2 = remote_pb2.RemoteData()

        print(d2, type(d2))

        d2.ParseFromString(d.SerializeToString())

        print(d2, type(d2))

if __name__ == "__main__":
    # Teensy.test_serialize()

    t = Teensy(80, "192.168.1.125")

    while True:
        t.sendRemoteData(random.random(), 2, 0, 50*random.random(), 5, 3178.3231, -0.0124)
        time.sleep(1)


import time
import sys
from typing import Type

sys.path.append('triad_openvr/')
import triad_openvr

class Vive:
    def __init__(self):
        self.v = triad_openvr.triad_openvr()
        self.v.print_discovered_objects()

        self.roll = 0
        self.pitch = 0
        self.yaw = 0

    def update(self):
        dat = self.v.devices["tracker_1"].get_pose_euler()

        try:
            self.yaw   = dat[3]
            self.pitch = dat[4]
            self.roll  = dat[5]
        except TypeError:
            pass

        self.printstate()

    def printstate(self):
        txt = ""
        for each in [self.roll, self.pitch, self.yaw]:
            txt += "%.4f" % each
            txt += " "
        print("\r" + txt, end="")

if __name__ == "__main__":
    vive = Vive()
    while True:
        vive.update()
        vive.printstate()
        time.sleep(0.01)

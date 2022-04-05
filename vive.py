import time
import sys
from typing import Type
import threading

import numpy as np

sys.path.append('triad_openvr/')
import triad_openvr

class Vive:
    def __init__(self, interval=1/250, N=2, debug=False):
        self.v = triad_openvr.triad_openvr()
        self.v.print_discovered_objects()

        self.interval = interval
        self.debug = debug

        self.N = N

        self._roll =  np.zeros(self.N)
        self._pitch = np.zeros(self.N)
        self._yaw =   np.zeros(self.N)

        self.i = 0

    def roll(self):
        return np.average(self._roll)

    def pitch(self):
        return np.average(self._pitch)

    def yaw(self):
        return np.average(self._yaw)

    def update(self):
        dat = self.v.devices["tracker_1"].get_pose_euler()

        try:
            self._yaw[self.i]   = dat[3]
            self._pitch[self.i] = dat[4]
            self._roll[self.i]  = dat[5]
        except TypeError:
            pass

        self.i = (self.i + 1) % self.N

        if self.debug:
            self.printstate()

    def printstate(self):
        txt = ""
        for each in [self.roll(), self.pitch(), self.yaw()]:
            txt += "%5.1f" % each
            txt += " "
        print("\r" + txt, end="")

    def loop(self):
        while True:
            start = time.time()
            self.update()
            sleep_time = self.interval-(time.time()-start)
            if sleep_time > 0:
                time.sleep(sleep_time)

    def start(self):
        self.t = threading.Thread(target=self.loop, daemon=True)
        self.t.start()

if __name__ == "__main__":
    vive = Vive(debug=True, N=1, interval=0)
    vive.start()
    while True:
        continue
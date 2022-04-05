import time
import sys
from typing import Type
import threading

sys.path.append('triad_openvr/')
import triad_openvr

class Vive:
    def __init__(self, interval=1/250, debug=False):
        self.v = triad_openvr.triad_openvr()
        self.v.print_discovered_objects()

        self.roll = 0
        self.pitch = 0
        self.yaw = 0

        self.interval = interval
        self.debug = debug

    def update(self):
        dat = self.v.devices["tracker_1"].get_pose_euler()

        try:
            self.yaw   = dat[3]
            self.pitch = dat[4]
            self.roll  = dat[5]
        except TypeError:
            pass

        if self.debug:
            self.printstate()

    def printstate(self):
        txt = ""
        for each in [self.roll, self.pitch, self.yaw]:
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
    vive = Vive(debug=True)
    vive.start()
    while True:
        continue
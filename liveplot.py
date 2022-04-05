import pyqtgraph as pg
import numpy as np

class Liveplot:
    def __init__(self, title, num_samples):
        self.x = np.linspace(0, num_samples, num_samples)
        self.num_samples = num_samples

        self.plotdat = np.zeros(self.num_samples)

        self.plot = pg.plot(title=title)
        self.curve = self.plot.plot(self.x, self.plotdat)

        self.i = 0

    def update(self, dat):
        self.plotdat[self.i] = dat
        self.i = (self.i + 1) % self.num_samples

        y1 = self.plotdat[:self.i]
        y2 = self.plotdat[self.i:]

        self.curve.setData(self.x, np.append(y2, y1))
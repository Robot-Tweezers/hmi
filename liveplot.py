import pyqtgraph as pg
import numpy as np

class Liveplot:
    def __init__(self, title, num_samples, legend, ndim=1):
        self.x = np.linspace(-num_samples, 0, num_samples)
        self.num_samples = num_samples

        self.ndim = ndim

        self.plotdat = [np.zeros(self.num_samples) for i in range(ndim)]

        # PyQtGraph
        self.plot = pg.plot(title=title)
        self.plot.addLegend()

        self.curves = []
        for j in range(ndim):
            self.curves.append(self.plot.plot(self.x, self.plotdat[j], pen=(j,3), name=legend[j]))

        self.i = 0

    def update(self, dat):
        for j in range(self.ndim):
            self.plotdat[j][self.i] = dat[j]

        self.i = (self.i + 1) % self.num_samples

        for j in range(self.ndim):
            y1 = self.plotdat[j][:self.i]
            y2 = self.plotdat[j][self.i:]

            self.curves[j].setData(self.x, np.append(y2, y1))

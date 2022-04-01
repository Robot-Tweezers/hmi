from multiprocessing import Process, Lock
import multithreading
import PySimpleGUI as sg
from time import sleep

class SharedData:
    def __init__(self):
        self.lock = Lock()
        self.gain = 0

class GUIchild:
    def __init__(self, sharedata):
        self.layout = [
                    [sg.Text('Some text on Row 1')],
                    [sg.Text('Enter something on Row 2'), sg.InputText()],
                    [sg.Button('Ok'), sg.Button('Cancel')]]

        self.window = sg.Window('Control Panel', self.layout)

        self.sd = sharedata

    def update(self):
        print("Starting child")
        while True:
            print("Doing")
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                raise RuntimeError("Window Closed")
            print('You entered ', values[0])

            self.sd.lock.acquire()
            try:
                self.sd.gain = values[0]
            finally:
                self.sd.lock.release()

            sleep(1)

class GUI:
    def __init__(self):
            self.sd = SharedData()
            self.child = GUIchild(self.sd)

            # self.child.update()
            self.p = Process(target=self.child.update)
            self.p.start()

    def getDat(self):
        g = 0
        self.sd.lock.acquire()
        try:
            g = self.sd.gain
        finally:
            self.sd.lock.release()

        return g

if __name__ == "__main__":
    g = GUI()

    for i in range(10):
        d = g.getDat()
        print(f"Data {i:2} is: {d}")
        sleep(1)

    g.p.join()

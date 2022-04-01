# import multithreading
import PySimpleGUI as sg
from time import sleep
import threading

from serial import SerialException
from serialparser import Serialparser
from HMI_server import HMIServer

class GUI:
    def __init__(self, server):
        self.layout = [
            [sg.Text("Robot Tweezers HMI GUI")],
            # [sg.Text("Connected to: " + port.name), sg.Button("Reconnect")],
            [sg.Text("Actuator Settings"), sg.InputText(key="actuator_settings")],
            [sg.Text("Roll Angle"), sg.InputText(key="roll", default_text=3.1415, size=(15, 30))],
            [sg.Text("Pitch Angle"), sg.InputText(key="pitch", default_text=0, size=(15, 30))],
            [sg.Text("Yaw Angle"), sg.InputText(key="yaw", default_text=0, size=(15, 30))],
            [sg.Button("Go")]
        ]

        self.window = sg.Window('Control Panel', self.layout)

        self.server = server

    def start(self):
        while True:
            print("GUI window")
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                raise RuntimeError("Window Closed")
            print('You entered ', values[0])

            self.server.gain = values[0]

if __name__ == "__main__":

    try:
        s = Serialparser("/dev/cu.usbmodem14101", 9600)
    except SerialException:
        s = None
        print("Serial not connected! Using full GUI mode")
    h = HMIServer(0, 0, 0, s)

    g = GUI(h)

    server = threading.Thread(target=h.start, daemon=True)


    server.start()
    g.start()
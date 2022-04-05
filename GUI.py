# import multithreading
from re import S
import PySimpleGUI as sg
from time import sleep
import threading

import pyqtgraph as pg
import numpy as np

from serial import SerialException
from liveplot import Liveplot
from serialparser import Serialparser
from HMI_server import HMIServer
from vive import Vive

class GUI:
    def __init__(self, server):
        self.layout = [
            [sg.Text("Robot Tweezers HMI GUI")],
            # [sg.Text("Connected to: " + port.name), sg.Button("Reconnect")],
            # [sg.Text("Actuator Settings"), sg.InputText(key="actuator_settings")],
            [sg.Text("Vive Rotation Data", size=(20,1)), sg.Text("Output Rotation Data", size=(20,1))],
            [sg.Text("Roll Angle:  ", size=(10,1)), sg.Text(size=(20,1), key='rolltxt'),sg.Text(key='rollout') ],
            [sg.Text("Pitch Angle: ", size=(10,1)), sg.Text(size=(20,1), key='pitchtxt'), sg.Text(key='pitchout')],
            [sg.Text("Yaw Angle:   ", size=(10,1)), sg.Text(size=(20,1), key='yawtxt'), sg.Text(key='yawout')],
            [sg.Button("Home Arm")],
            [sg.Text("Rotation Reduction Ratio:", size=(15,2)),
                sg.Sl(range=(1,10), default_value=1, orientation='horizontal', enable_events=True,
                key="gainslider")]
        ]

        self.window = sg.Window('Control Panel', self.layout)

        self.server = server

        self.plot = Liveplot("Vive Roll", 200, ndim=3)
        self.plot.plot.setYRange(-180, 180)

    def start(self):
        while True:
            event, values = self.window.read(timeout=10)
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
            if event == "Home Arm":
                print("Homing the arm")
            if event == "gainslider":
                self.server.gain = 1/float(values["gainslider"])

            roll = self.server.vive.roll()
            pitch = self.server.vive.pitch()
            yaw = self.server.vive.yaw()

            self.window['rolltxt'].update(f'{roll:4.0f}')
            self.window['pitchtxt'].update(f'{pitch:4.0f}')
            self.window['yawtxt'].update(f'{yaw:4.0f}')

            self.window['rollout'].update(f'{self.server.roll:4.2f}')
            self.window['pitchout'].update(f'{self.server.pitch:4.2f}')
            self.window['yawout'].update(f'{self.server.yaw:4.2f}')

            self.plot.update([roll, pitch, yaw])

if __name__ == "__main__":

    try:
        s = Serialparser("/dev/cu.usbmodem14101", 9600)
    except SerialException:
        s = None
        print("Serial not connected! Using full GUI mode")

    vive = Vive()

    h = HMIServer("192.168.1.212", 80, vive, s, debug=True)

    print("HMI server setup")

    g = GUI(h)

    server = threading.Thread(target=h.start, daemon=True)

    vive.start()
    server.start()
    g.start()

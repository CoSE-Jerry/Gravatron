from time import sleep
from PyQt5.QtCore import QThread
from picamera import PiCamera
from Main import *

class Snap(QThread):

    def __init__(self):
         QThread.__init__(self)

    def __del__(self):
         self._running = False

    def run(self):
        with PiCamera() as camera:
            camera.resolution = (2464,2464)
            camera.capture("../_temp/snapshot.jpg")
            
class Live(QThread):

    def __init__(self):
         QThread.__init__(self)

    def __del__(self):
         self._running = False

    def run(self):
        with PiCamera() as camera:
            camera.start_preview()
            sleep(30)
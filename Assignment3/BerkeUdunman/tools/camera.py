# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022

from OpenGL.raw.GLU import gluLookAt


# References:
# - https://stackoverflow.com/questions/5717654/glulookat-explanation

class Camera:
    def __init__(self, position):
        self.position = position
        self.x_cam = position[0]
        self.y_cam = position[1]
        self.z_cam = position[2]

    def cameraUpdate(self):
        gluLookAt(self.x_cam, self.y_cam, self.z_cam, 0, 0, 0, 0, 1, 0)


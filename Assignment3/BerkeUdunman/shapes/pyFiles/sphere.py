# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022
# Version 2

# References:
# - http://www.songho.ca/opengl/gl_sphere.html
#
import math

from vec3d import Vec3d
from OpenGL.GL import GL_POLYGON


class Sphere:

    def __init__(self, radius=1, latitude_divisions=40, longitude_divisions=40):

        self.radius = radius
        self.latitude_divisions = latitude_divisions
        self.longitude_divisions = longitude_divisions

        self.vertices = []

        for latitude in range(latitude_divisions + 1):
            theta = latitude * math.pi / latitude_divisions
            sintheta = math.sin(theta)
            costheta = math.cos(theta)
            for longitude in range(longitude_divisions + 1):
                phi = longitude * 2 * math.pi / longitude_divisions
                sinphi = math.sin(phi)
                cosphi = math.cos(phi)

                x = cosphi * sintheta
                y = costheta
                z = sinphi * sintheta

                self.vertices.append(Vec3d(x * radius, y * radius, z * radius, 1))

        self.facesLine = []
        self.planeShapes = []
        for latitude in range(latitude_divisions):
            for longitude in range(longitude_divisions):
                i = latitude * (longitude_divisions + 1) + longitude
                j = i + longitude_divisions + 1
                self.facesLine.append([
                    i + 1,
                    j,
                    i,
                    i + 1,
                    j + 1,
                    j,
                ])
                self.planeShapes.append(GL_POLYGON)

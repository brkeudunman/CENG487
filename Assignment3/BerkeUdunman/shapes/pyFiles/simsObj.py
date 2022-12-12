# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022

from vec3d import Vec3d

from OpenGL.GL import GL_POLYGON


class SimsPyramid:
    def __init__(self):
        self.vertices = [
            Vec3d(0, 0, 0.5, 1),  # 0
            Vec3d(0.5, 0, 0, 1),  # 1

            Vec3d(0, 0, -0.5, 1),  # 2
            Vec3d(-0.5, 0, 0, 1),  # 3

            Vec3d(0, 1, 0, 1),  # 4
            Vec3d(0, -1, 0, 1)  # 5
        ]

        self.facesLine = [[0, 4, 1], [1, 4, 2], [2, 4, 3], [3, 4, 0], [0, 5, 1], [1, 5, 2], [2, 5, 3], [3, 5, 0]]
        self.planeShapes = [GL_POLYGON, GL_POLYGON, GL_POLYGON, GL_POLYGON, GL_POLYGON, GL_POLYGON, GL_POLYGON,
                            GL_POLYGON]

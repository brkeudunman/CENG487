# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022
from OpenGL.GL import *
import random

from obj import Obj


class Slicer:
    # This class slice the 3d objects

    @staticmethod
    def sliceModel(model3d):
        # - Model is a three-dimensional plane array.
        # - With outer for loop, I traverse the quad plane count
        # - With inner for loop, I traverse the quad plane's points
        # - At the end of the inner loop, we have a 2d plane with vertices,color,shape and matrixStack. Also, we add the
        #   2d plane to the planeArray.
        # - Finally, at the end of the method, we call the another method to append our planes to scene.
        planeArray = []
        print(model3d.facesLine)
        for i in range(len(model3d.facesLine)):
            shape = GL_TRIANGLE_FAN
            plane = Obj(vertices=[],
                        matrixStack=[

                        ],
                        shape=shape,
                        color=[random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)])
            for j in range(len(model3d.facesLine[i])):
                index = model3d.facesLine[i][j]
                plane.vertices.append(model3d.vertices[index])
            planeArray.append(plane)
        return planeArray

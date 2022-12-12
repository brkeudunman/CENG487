# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022
# Version 2

import time
from tools.slicer import Slicer
from mat3d import Mat3d
from obj import Obj
from OpenGL.GL import *
from OpenGL.GLUT import *


class Scene:

    def __init__(self, objArray):
        self.objArray = objArray
        self.modelArray = []

    def appendObjectToScene(self, obj):
        self.objArray.append(obj)

    def removeObjectFromScene(self, obj):
        self.objArray.remove(obj)

    def appendModelToScene(self,model):
        self.modelArray.append(model)

    def clearScene(self):
        self.objArray = []

    def drawScene(self):
        for obj in self.objArray:
            Scene.drawShape(obj)
 
    def drawModelByIndex(self,i):
        if(i>len(self.modelArray)-1):
            print("Index Out Of Range, please try again")
        else:
            self.drawModel(self.modelArray[i])
            
    def drawModel(self, model3d):
        slicedPlanes = Slicer.sliceModel(model3d)
        for plane in slicedPlanes:
            self.appendObjectToScene(plane)

    def rotateObj(self, radian, signFlag=1):
        for obj in self.objArray:
            obj.addTransformation(Mat3d.getRotationXMatrix(radian, signFlag))

    @staticmethod
    def drawShape(obj: Obj):
        glBegin(obj.shape)
        Scene.paintObj(obj)
        for vertex in obj.vertices:
            glVertex3f(vertex.x, vertex.y, vertex.z)
        Scene.applyTransformations(obj)
        glEnd()

    @staticmethod
    def paintObj(obj: Obj):
        # Paint the obj
        glColor3f(obj.color[0], obj.color[1], obj.color[2])

    @staticmethod
    def applyTransformations(obj: Obj):
        # Traverse the object's matrixStack for apply transformation matrices
        cursor = len(obj.matrixStack) - 1
        result = Mat3d.getIdentityMatrix()
        while cursor != -1:
            result = result.multiply(obj.matrixStack[cursor])
            cursor -= 1
        counter = 0
        for vertex in obj.vertices:
            vertex = result.multiplyWithVector(vertex)
            obj.vertices[counter] = vertex
            counter += 1
        return obj
    
    @staticmethod
    def text(x, y, color, text):
        glColor3fv(color)
        glWindowPos2f(x, y)
        glutBitmapString(GLUT_BITMAP_TIMES_ROMAN_24, text.encode('ascii'))


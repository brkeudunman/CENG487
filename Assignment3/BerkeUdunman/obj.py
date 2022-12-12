# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022
# Version 2
class Obj:

    def __init__(self, vertices, matrixStack, shape, color):
        self.vertices = vertices
        self.matrixStack = matrixStack
        self.shape = shape
        self.color = color
        self.faces = []

    def addTransformation(self, transformationMatrix):
        self.matrixStack.append(transformationMatrix)

    def popTransformation(self):
        self.matrixStack.pop()

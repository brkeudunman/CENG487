# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022
# Version 2

from tools.parser import Parser
from vec3d import Vec3d


class Cube:

    def __init__(self):
        parser = Parser()
        parsedValues = parser.parse(objfile="ecube")
        self.vertices = parsedValues[0]
        self.facesLine = parsedValues[1]
        self.subDivisionCount = 1
        
    @staticmethod
    def getMidpoint(v1, v2):
        # Calculate the midpoint between the two vertices and return it
        return Vec3d((v1.x + v2.x) / 2, (v1.y + v2.y) / 2, (v1.z + v2.z) / 2, 1)

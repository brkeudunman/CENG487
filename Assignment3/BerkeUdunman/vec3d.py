# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022

import math


class Vec3d:

    # Initialization functions
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return f"[{self.x}|\n|{self.y}|\n|{self.z}|\n|{self.w}]"

    # Vector and Point manipulation operations like

    def dotProduct(self, vec3d):
        return (self.x * vec3d.x) + (self.y * vec3d.y) + (self.z * vec3d.z) + (self.w * vec3d.w)

    def crossProduct(self, vec3d):
        return Vec3d((self.y * vec3d.z - self.z * vec3d.y),
                     (self.z * vec3d.x - self.x * vec3d.z),
                     (self.x * vec3d.y - self.y * vec3d.x), 1)

    def projection(self, vec3d):
        # Projection Formula = (  a.b ( dot product of two vector ) / b's magnitude ) x (Scalar Multiplication) unit
        # vector of b.

        unitVector = vec3d.getUnitVector()

        constantX = (self.dotProduct(  # dot product of a and b divided by b's magnitude
            vec3d) / vec3d.calculateMagnitude())

        return unitVector.scalarMultiplication(constantX)

    def calculateAngleRadian(self, vec3d):
        dotProduct = self.dotProduct(vec3d)
        magnitude_self = self.calculateMagnitude()
        magnitude_vec3d = vec3d.calculateMagnitude()
        cosAlpha = dotProduct / (magnitude_self * magnitude_vec3d)

        return math.acos(cosAlpha)  # Result in radian

    def calculateAngleDegree(self, vec3d):
        pi = 22 / 7
        radian = self.calculateAngleRadian(vec3d)
        degree = radian * (180 / pi)
        return degree

    def getUnitVector(self):
        return self.scalarDivision(self.calculateMagnitude())

        # Arithmetic Operations

    def addWithVector(self, vec3d):
        self.x = self.x + vec3d.x
        self.y = self.y + vec3d.y
        self.z = self.z + vec3d.z

        return self

    def subtractWithVector(self, vec3d):
        self.x = self.x - vec3d.x
        self.y = self.y - vec3d.y
        self.z = self.z - vec3d.z

        return self

    def scalarMultiplication(self, number):
        self.x *= number
        self.y *= number
        self.z *= number

        return self

    def scalarDivision(self, number):
        self.x /= number
        self.y /= number
        self.z /= number

        return self

    def calculateMagnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    # Get Methods

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getW(self):
        return self.w

    def getCoordinates(self):
        return [self.x, self.y, self.z]

    # Initialized base vectors static methods
    @staticmethod
    def getBaseVectorXAxis():
        return Vec3d(1, 0, 0, 0)

    @staticmethod
    def getBaseVectorYAxis():
        return Vec3d(0, 1, 0, 0)

    @staticmethod
    def getBaseVectorZAxis():
        return Vec3d(0, 0, 1, 0)

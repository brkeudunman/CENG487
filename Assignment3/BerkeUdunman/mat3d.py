# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022
import math
from vec3d import Vec3d


class Mat3d:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        row1 = f"{self.matrix[0].getX()} | {self.matrix[0].getY()} | {self.matrix[0].getZ()} | {self.matrix[0].getW()}"
        row2 = f"{self.matrix[1].getX()} | {self.matrix[1].getY()} | {self.matrix[1].getZ()} | {self.matrix[1].getW()}"
        row3 = f"{self.matrix[2].getX()} | {self.matrix[2].getY()} | {self.matrix[2].getZ()} | {self.matrix[2].getW()}"
        row4 = f"{self.matrix[3].getX()} | {self.matrix[3].getY()} | {self.matrix[3].getZ()} | {self.matrix[3].getW()}"
        return f"{row1}\n{row2}\n{row3}\n{row4}"

    def transpose(self):
        return Mat3d(
            [Vec3d(self.matrix[0].x, self.matrix[1].x, self.matrix[2].x, self.matrix[3].x),
             Vec3d(self.matrix[0].y, self.matrix[1].y, self.matrix[2].y, self.matrix[3].y),
             Vec3d(self.matrix[0].z, self.matrix[1].z, self.matrix[2].z, self.matrix[3].z),
             Vec3d(self.matrix[0].w, self.matrix[1].w, self.matrix[2].w, self.matrix[3].w)]
        )

    def multiplyWithVector(self, vec3d):
        # Multiply 4x4 matrix by 4x1 vector
        return Vec3d(self.matrix[0].dotProduct(vec3d),
                     self.matrix[1].dotProduct(vec3d),
                     self.matrix[2].dotProduct(vec3d),
                     1)

    def multiply(self, matrix):
        # Multiply 4x4 matrix by 4x4 matrix
        matrix = matrix.transpose()
        array = []
        for i in range(4):
            vec3d = Vec3d(self.matrix[i].dotProduct(matrix.matrix[0]), self.matrix[i].dotProduct(matrix.matrix[1]),
                          self.matrix[i].dotProduct(matrix.matrix[2]), self.matrix[i].dotProduct(matrix.matrix[3]))
            array.append(vec3d)
        return Mat3d(array)

    @staticmethod
    def getTranslationMatrix(dx, dy, dz, flag=1):
        # Flag indicates if it's inverse or not.
        # Initially flag is defined by one. If it's inversed , the flag should be -1.
        if (flag == 1) or (flag == -1):
            return Mat3d([Vec3d(1, 0, 0, flag * dx),
                          Vec3d(0, 1, 0, flag * dy),
                          Vec3d(0, 0, 1, flag * dz),
                          Vec3d(0, 0, 0, 1)])
        else:
            print("The flag must be 1 or -1\nFunction returning false...")
            return False

    @staticmethod
    def getScalingMatrix(sx, sy, sz, flag=1):  # Flag indicates if it's inverse or not.
        # Initially flag is defined by one. If it's inversed , the flag should be -1.
        if (flag == 1) or (flag == -1):
            return Mat3d([Vec3d(sx ** flag, 0, 0, 0),
                          Vec3d(0, sy ** flag, 0, 0),
                          Vec3d(0, 0, sz ** flag, 0),
                          Vec3d(0, 0, 0, 1)])
        else:
            print("The flag must be 1 or -1\nFunction returning false...")
            return False

    @staticmethod
    def getRotationXMatrix(angleRadian, flag=1):
        # Flag indicates if it's inverse or not.
        # Initially flag is defined by one. If it's inversed , the flag should be -1.
        if (flag == 1) or (flag == -1):
            return Mat3d([Vec3d(1, 0, 0, 0),
                          Vec3d(0, math.cos(angleRadian), -math.sin(angleRadian) * flag, 0),
                          Vec3d(0, math.sin(angleRadian) * flag, math.cos(angleRadian), 0),
                          Vec3d(0, 0, 0, 1)])
        else:
            print("The flag must be 1 or -1\nFunction returning false...")
            return False

    @staticmethod
    def getRotationYMatrix(angleRadian, flag=1):
        # Flag indicates if it's inverse or not.
        # Initially flag is defined by one. If it's inversed , the flag should be -1.
        if (flag == 1) or (flag == -1):
            return Mat3d([Vec3d(math.cos(angleRadian), 0, math.sin(angleRadian) * flag, 0),
                          Vec3d(0, 1, 0, 0),
                          Vec3d(-math.sin(angleRadian) * flag, 0, math.cos(angleRadian), 0),
                          Vec3d(0, 0, 0, 1)])
        else:
            print("The flag must be 1 or -1\nFunction returning false...")
            return False

    @staticmethod
    def getRotationZMatrix(angleRadian, flag=1):
        # Flag indicates if it's inverse or not.
        # Initially flag is defined by one. If it's inversed , the flag should be -1.
        if (flag == 1) or (flag == -1):
            return Mat3d([Vec3d(math.cos(angleRadian), -math.sin(angleRadian) * flag, 0, 0),
                          Vec3d(math.sin(angleRadian) * flag, math.cos(angleRadian), 0, 0),
                          Vec3d(0, 0, 1, 0),
                          Vec3d(0, 0, 0, 1)])
        else:
            print("The flag must be 1 or -1\nFunction returning false...")
            return False

    @staticmethod
    def getIdentityMatrix():
        return Mat3d([Vec3d(1, 0, 0, 0),
                      Vec3d(0, 1, 0, 0),
                      Vec3d(0, 0, 1, 0),
                      Vec3d(0, 0, 0, 1)])

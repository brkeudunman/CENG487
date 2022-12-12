# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022

from tools.parser import Parser
from vec3d import Vec3d


class Cube:

    def __init__(self):
        parser = Parser()
        parsedValues = parser.parse(objfile="ecube")
        self.vertices = parsedValues[0]
        self.facesLine = parsedValues[1]
        self.subDivisionCount = 1

    def subdivide(self, numSubdivisions):
        # Create a new list of vertices, which will be the result of the subdivisions
        newVertices = []

        # Loop over all of the faces in the cube
        for face in self.facesLine:
            # Create a list of new vertices for the current face
            faceVertices = []

            # Loop over all of the vertices in the face
            for i in range(len(face)):
                # Get the vertex at the current position
                vertex = self.vertices[face[i]]

                # Add the vertex to the list of vertices for the current face
                faceVertices.append(vertex)

                # If this is not the last vertex in the face, get the next vertex
                # in the face and add the midpoint between the two vertices to the
                # list of vertices for the current face
                if i < len(face) - 1:
                    nextVertex = self.vertices[face[i + 1]]
                    midpoint = self.getMidpoint(vertex, nextVertex)
                    faceVertices.append(midpoint)

                # If this is the last vertex in the face, get the first vertex
                # in the face and add the midpoint between the two vertices to the
                # list of vertices for the current face
                else:
                    firstVertex = self.vertices[face[0]]
                    midpoint = self.getMidpoint(vertex, firstVertex)
                    faceVertices.append(midpoint)

            # Add the new vertices for the current face to the list of new vertices
            newVertices.extend(faceVertices)

        # Set the list of vertices for the cube to be the new list of vertices
        self.vertices = newVertices

        # If we have not reached the desired number of subdivisions, perform
        # one more level of subdivisions
        if numSubdivisions > 1:
            self.subdivide(numSubdivisions - 1)

    @staticmethod
    def getMidpoint(v1, v2):
        # Calculate the midpoint between the two vertices and return it
        return Vec3d((v1.x + v2.x) / 2, (v1.y + v2.y) / 2, (v1.z + v2.z) / 2, 1)

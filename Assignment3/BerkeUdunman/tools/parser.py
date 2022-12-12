# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022
# Version 2

from vec3d import Vec3d


class Parser:
    # This class stands for parse the obj files in shapes folder.
    # References of this class :
    # - https://stackoverflow.com/questions/40107359/obj-file-parser-with-opengl

    def __init__(self):
        self.verticesArr = []
        self.faceArr = []

    def parse(self, objfile=None):
        # Open the file and read each line
        with open(f'./shapes/objFiles/{objfile}.obj', 'r') as f:
            lines = f.readlines()

        # Iterate over each line in the file
        for line in lines:
            # Split the line into individual words
            words = line.split()

            if words:
                # If the first word is 'v', it indicates a vertex
                if words[0] == 'v':
                    # extract the coordinates from the line and convert them to floats
                    x = float(words[1])
                    y = float(words[2])
                    z = float(words[3])
                    # add the vertex to the list of vertices
                    self.verticesArr.append(Vec3d(x, y, z, 1))

                # If the first word is 'f', it indicates a face
                if words[0] == 'f':
                    # extract the vertex indices from the line and convert them to integers
                    v1 = int(words[1]) - 1
                    v2 = int(words[2]) - 1
                    v3 = int(words[3]) - 1
                    v4 = int(words[4]) - 1

                    # Add the face to the list of faces
                    self.faceArr.append([v1, v2, v3, v4])

        # Print the number of vertices and faces
        print(len(self.verticesArr), 'vertices')
        print(len(self.faceArr), 'faces')

        return [self.verticesArr, self.faceArr]


parser = Parser()

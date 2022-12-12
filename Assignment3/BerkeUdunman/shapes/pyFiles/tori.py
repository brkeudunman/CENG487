# CENG 487 Assignment3 by
# Berke Udunman
# StudentNo: 270201046
# Date: 12-2022
# Version 2

from tools.parser import Parser


class Tori:
    def __init__(self):
        parser = Parser()
        parsedValues = parser.parse(objfile="tori")
        self.vertices = parsedValues[0]
        self.facesLine = parsedValues[1]
        self.subDivisionCount = 1

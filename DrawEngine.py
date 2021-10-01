import os

class DrawEngine:
    def __init__(self, vw, vh):
        self.width = vw
        self.height = vh
        self.__rowLength = vw + 1
        self.__bufferSize = vh * self.__rowLength
        self.__buffer = [" " for i in range(self.__bufferSize)]
        self.clearBuffer()

    def draw(self):
        os.system("clear")
        print("".join(self.__buffer))

    def setPixel(self, x, y, pixel):
        if (x >= self.width or y >= self.height):
            return
        index = y * self.__rowLength + x
        self.__buffer[index] = pixel

    def clearBuffer(self):
        for i in range(self.__bufferSize):
            if (i + 1 - i // self.width) % (self.width) == 0:
                self.__buffer[i] = "\n"
            else:
                self.__buffer[i] = " "

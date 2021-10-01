from DrawEngine import DrawEngine
from ControlAndPhisics import ControlAndPhisics

from time import sleep
from math import sin, cos, sqrt

DEFAULT_FOV = 3.14159 / 4.0
DEFAULT_PLAYER_X = 1.5
DEFAULT_PLAYER_Y = 3
DEFAULT_PLAYER_ALPHA = 1.5

WALL_TEXTURES = [
    "\u2588",
    "\u2593",
    "\u2592",
    "\u2591"
]

class Camera:
    def __init__(self, x, y, alpha):
        self.x = x
        self.y = y
        self.alpha = alpha

    def move(self, dx = 0, dy = 0):
        self.x += dx
        self.y += dy

    def rotate(self, dalpha):
        self.alpha += dalpha

class GraphicsEngine:
    def __init__(
        self,
        width,
        height,
        map,
        x = DEFAULT_PLAYER_X,
        y = DEFAULT_PLAYER_Y,
        alpha = DEFAULT_PLAYER_ALPHA,
        fov = DEFAULT_FOV
    ):
        self.__drawEngine = DrawEngine(width, height)
        self.__camera = Camera(x, y, alpha)
        self.__control = ControlAndPhisics(self.__camera, map)
        self.__map = map
        self.__fov = fov

    def __makeFrame(self):
        setPixel = self.__drawEngine.setPixel
        width = self.__drawEngine.width
        height = self.__drawEngine.height
        currAngle = self.__camera.alpha - self.__fov / 2
        dAngle = self.__fov / width
        step = 0.1
        for x in range(width):
            currX = self.__camera.x
            currY = self.__camera.y
            distance = 0
            while distance < 50:
                currX += cos(currAngle) * step
                currY -= sin(currAngle) * step
                if (self.__map[int(currY)][int(currX)] != " "):
                    wallTexture = " "
                    distance = sqrt((currX - self.__camera.x) ** 2 + (currY - self.__camera.y) ** 2)

                    if distance < 2:
                        wallTexture = WALL_TEXTURES[0]
                    elif distance < 4:
                        wallTexture = WALL_TEXTURES[1]
                    elif distance < 6:
                        wallTexture = WALL_TEXTURES[2]
                    else:
                        wallTexture = WALL_TEXTURES[3]

                    break
            wallHeight = height / distance
            wallStart = (height - wallHeight) / 2
            if wallStart < 0:
                wallStart = 0
            wallEnd = height - wallStart
            for y in range(height):
                if y > wallStart and y < wallEnd:
                    setPixel(x, y, wallTexture)
                else:
                    setPixel(x, y, " ")
            currAngle += dAngle


    def run(self):
        while True:
            self.__control.inputHnadle()
            self.__makeFrame()
            self.__drawEngine.draw()
            sleep(0.07)






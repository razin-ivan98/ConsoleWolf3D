from typing import MutableMapping
import keyboard
from math import sin, cos

MOVE_STEP = 0.4
ROTATE_STEP = 0.1

class ControlAndPhisics:
    def __init__(self, camera, map):
        self.__camera = camera
        self.__map = map

    def __canMove(self, x, y):
        if self.__map[int(y)][int(x)] == " ":
            return True
        return False

    def inputHnadle(self):
        if keyboard.is_pressed('w'):
            dx = MOVE_STEP * cos(self.__camera.alpha)
            dy = -MOVE_STEP * sin(self.__camera.alpha)
            if (self.__canMove(self.__camera.x + dx, self.__camera.y + dy)):
                self.__camera.move(dx, dy)
        if keyboard.is_pressed('s'):
            dx = -MOVE_STEP * cos(self.__camera.alpha)
            dy = MOVE_STEP * sin(self.__camera.alpha)
            if (self.__canMove(self.__camera.x + dx, self.__camera.y + dy)):
                self.__camera.move(dx, dy)
        if keyboard.is_pressed('a'):
            self.__camera.rotate(-ROTATE_STEP)
        if keyboard.is_pressed('d'):
            self.__camera.rotate(ROTATE_STEP)
            
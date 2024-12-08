import math
import numpy as np

GRAVITY = 9.6


class Pendulum:
    def __init__(self, angle,  length, mass):
        self._angle = angle
        self._anglev = 0
        self._length = length
        self._mass = mass

    def update(self):
        force = GRAVITY * math.sin(self._angle)
        self._anglev += -1 * force
        self._angle += self._anglev

    @property
    def pos(self):
        x = self._length * math.sin(self._angle)
        y = self._length * math.cos(self._length)
        return np.array([x, y])

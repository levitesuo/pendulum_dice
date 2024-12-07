import math
import numpy as np


class Pendulum:
    def __init__(self):
        self._location = np.array((0, 0), dtype=float)

    @property
    def location(self):
        return self._location

    def set_location_from_angle(self, angle):
        new_location = np.array(
            (math.sin(angle), -math.cos(angle)), dtype=float)
        self._location = new_location

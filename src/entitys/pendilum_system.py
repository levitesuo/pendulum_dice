import math
import numpy as np

from entitys.pendilum import Pendulum


class PendulumSystem:
    def __init__(self):
        self._x_pendulum = Pendulum()
        self._y_pendulum = Pendulum()

        self._pendulums = [self._x_pendulum, self._y_pendulum]

    def set_locations_from_angle(self, angle):
        for i, pendulum in enumerate(self._pendulums):
            pendulum.set_location_from_angle(angle + i * math.pi/3)

    def get_head_location(self):
        return np.array([cord.location[i] for i, cord in enumerate(self._pendulums)])

import math
import numpy as np


class LineGenerator:
    def __init__(self, scal1, scal2, scal3):
        iterations = 300
        pos = np.zeros(shape=3, dtype=float)

        self._scalars = [scal1, scal2, scal3]
        self._points = np.empty([iterations+1, pos.shape[0]])

        l = 1
        offset = math.pi/3

        for i in range(iterations + 1):
            angle = i / iterations * 2 * math.pi
            pos = np.zeros(shape=3, dtype=float)
            for j, scal in enumerate([scal1, scal2, scal3]):
                a = angle * scal
                self._points[i][j] = l * math.sin(a + offset * j)

    @property
    def points(self):
        return self._points

import matplotlib.pyplot as plt


class PlottingService:
    def __init__(self):
        self._points = []

    def add_point(self, point):
        self._points.append(point)

    def show_plot(self):
        ax = plt.figure().add_subplot(projection='3d')
        xs = [cord[0] for cord in self._points]
        ys = [cord[1] for cord in self._points]
        zs = [cord[2] for cord in self._points]
        ax.plot(xs, ys, zs)
        plt.show()

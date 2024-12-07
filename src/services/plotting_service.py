import matplotlib.pyplot as plt


class PlottingService:
    def __init__(self):
        self._points = []

    def add_point(self, point):
        self._points.append(point)

    def show_plot(self):
        xs = [cord[0] for cord in self._points]
        ys = [cord[1] for cord in self._points]
        print(len(xs))
        plt.plot(xs, ys)
        plt.show()

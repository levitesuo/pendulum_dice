from services.line_generator import LineGenerator
from services.plotting_service import PlottingService

g = LineGenerator(11, 13, 9)
plotter = PlottingService()

plotter._points = g.points

plotter.show_plot()

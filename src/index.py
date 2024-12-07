import math

from services.plotting_service import PlottingService
from entitys.pendilum_system import PendulumSystem

pendulum = PendulumSystem()
plotter = PlottingService()

for i in range(40000):
    angle = math.sin(i/1000)
    angle2 = pendulum.get_head_location()[0]
    pendulum.set_locations_from_angle(angle)
    plotter.add_point([angle2, angle])

plotter.show_plot()

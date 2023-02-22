from matplotlib import pyplot as plt
from floodsystem.plot import plot_water_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime

def test_plot_water_levels():
    plot_water_levels(("1", "2"), ((1, 2, 3), (1, 2, 4)), ((3, 4, 6), (3, 5, 7)))
    plot_water_levels(("1", "2","3","4","5","6"), ((1, 2, 3), (1, 2, 4), (1, 2, 4), (1, 2, 4), (1, 2, 4), (1, 2, 10)), ((3, 4, 6), (3, 5, 7),(3, 5, 9),(3, 5, 7),(3, 5, 7),(3, 5, 7)))
    assert plot_water_levels(("1", "2","3","4","5","6","7"), ((1, 2, 3), (1, 2, 4), (1, 2, 4), (1, 2, 4), (1, 2, 4), (1, 2, 10), (1, 2, 10)), ((3, 4, 6), (3, 5, 7),(3, 5, 9),(3, 5, 7),(3, 5, 7),(3, 5, 7),(3, 5, 7))) == print("Too many stations.")
    assert plot_water_levels(("1", "2","3","4","5","6"), ((1, 2, 4), (1, 2, 4), (1, 2, 4), (1, 2, 4), (1, 2, 10)), ((3, 4, 6), (3, 5, 7),(3, 5, 9),(3, 5, 7),(3, 5, 7),(3, 5, 7))) == print("Number of stations do not match number of dates/levels.")

#test_plot_water_levels()

def test_plot_water_level_with_fit():
    x1 = [datetime(2010, 1, 1),datetime(2010, 1, 2),datetime(2010, 1, 3),datetime(2010, 1, 4),datetime(2010, 1, 5)]
    y1 = [1, 2, 3, 4, 5]
    plot_water_level_with_fit('test1', x1, y1, 2)

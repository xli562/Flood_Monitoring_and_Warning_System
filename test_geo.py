# Copyright (C) 2023 Xiaoyang Li
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from random import random, shuffle
from floodsystem.geo import stations_by_distance
from test_station import test_create_monitoring_station


def test_stations_by_distance():

    # Making sure the class is correctly set up
    test_create_monitoring_station()

    lst = []    # The list to contain the stations
    # Create 5 stations
    for i in range(5):
        station_id = "{i}"
        measure_id = "test-m-id-{i}"
        label = "some station_{i}"
        coord = (1.0 + 5.1*i, 4.0 - 4.9*i)
        trange = (-2.3 + random(), 3.4445 + random())
        river = "River {i}"
        town = "My Town {i}"
        s = MonitoringStation(station_id, measure_id, label, coord, trange, river, town)
        lst.append(s)
    
    shuffle(lst)
    lst = stations_by_distance(lst, (1.0,4.0))
    for i in range(5):
        assert int(lst[i].name) == i

    
    
    



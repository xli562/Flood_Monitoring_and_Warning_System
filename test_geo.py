# Copyright (C) 2023 Xiaoyang Li
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from random import random, shuffle
from floodsystem.geo import stations_by_distance, stations_within_radius
from test_station import test_create_monitoring_station


def test_stations_by_distance():

    # Making sure the class is correctly set up
    test_create_monitoring_station()

    lst = []    # The list to contain the stations
    # Create 5 stations
    for i in range(5):
        station_id = f"{i}"
        measure_id = f"test-m-id-{i}"
        label = f"some station_{i}"
        coord = (1.0 + 5.1*i, 4.0 - 4.9*i)
        trange = (-2.3 + random(), 3.4445 + random())
        river = f"River {i}"
        town = f"My Town {i}"
        s = MonitoringStation(station_id, measure_id, label, coord, trange, river, town)
        lst.append(s)
    
    shuffle(lst)
    lst = stations_by_distance(lst, (1.0,4.0))
    for i in range(5):
        assert int(lst[i].name) == i
    print('PASSED test_stations_by_distance()')


def test_stations_within_radius():
    
    # Making sure the class is correctly set up
    test_create_monitoring_station()

    sts = []    # The list to contain the stations [sts = stations]
    # Create 5 stations
    for i in range(5):
        station_id = f"{i}"
        measure_id = f"test-m-id-{i}"
        label = f"some station_{i}"
        coord = (1.0 + 5.1*i, 4.0 - 4.9*i)
        trange = (-2.3 + random(), 3.4445 + random())
        river = f"River {i}"
        town = f"My Town {i}"
        s = MonitoringStation(station_id, measure_id, label, coord, trange, river, town)
        sts.append(s)
    
    # Getting stations within radius [radSts = stations within radius]
    radSts = stations_within_radius(sts, (0,0), 1000)
    print(radSts)
    assert len(radSts) == 5
    for i in radSts:
        assert type(i) == MonitoringStation
    print('PASSED test_stations_within_radius()')


test_stations_within_radius()
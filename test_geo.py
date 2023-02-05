# Copyright (C) 2023 Xiaoyang Li
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from random import random, shuffle
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius
from test_station import test_create_monitoring_station
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from haversine import haversine
import numpy as np


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
        assert lst[i][0] == f'some station_{i}'
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
    radSts = stations_within_radius(sts, (0.0,1.0), 10000)
    assert len(radSts) == 5
    for i in radSts:
        assert type(i) == MonitoringStation
    print('PASSED test_stations_within_radius()')


def test_rivers_by_station_number():

    toomanyrivers = []

    for station in build_station_list():
        if station.river == 'River Thames':
            toomanyrivers.append(station.name)
    sts = [('River Thames', len(toomanyrivers))]

    assert rivers_by_station_number(build_station_list(), 1) == sts
    print('PASSED test_rivers_by_station_number()')


def test_rivers_with_station():

    i = 0
    for station in build_station_list():
       assert station.river in rivers_with_station(build_station_list())
       i += 1
       if i == 10:
        break
    print('PASSED test_rivers_with_station()')


def test_stations_by_river():
    a = build_station_list()
    b = a[np.random.randint(0,len(a))]

    sts = stations_by_river(build_station_list())

    assert type(sts[b.river]) == set
    print('PASSED test_stations_by_river()')

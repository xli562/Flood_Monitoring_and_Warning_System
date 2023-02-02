# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():
    # Making sure the class is correctly set up
    test_create_monitoring_station()

    for i in range(5):
        station_id = f"{i}"
        measure_id = f"test-m-id-{i}"
        label = f"some station_{i}"
        coord = (1.0 + 5.1*i, 4.0 - 4.9*i)
        trange = (10+i, -5+0.5*i)
        river = f"River {i}"
        town = f"My Town {i}"
        s = MonitoringStation(station_id, measure_id, label, coord, trange, river, town)
        assert s.typical_range_consistent() == False

    for i in range(5):
        station_id = f"{i}"
        measure_id = f"test-m-id-{i}"
        label = f"some station_{i}"
        coord = (4.0 - 4.9*i, 1.0 + 5.1*i)
        trange = (1.0+0.01*i, 9+i)
        river = f"River {i}"
        town = f"My Town {i}"
        s = MonitoringStation(station_id, measure_id, label, coord, trange, river, town)
        assert s.typical_range_consistent() == True


def test_inconsistent_typical_range_stations():
    # Making sure the class is correctly set up
    test_create_monitoring_station()
    lst = []

    for i in range(5):
        station_id = f"{i}"
        measure_id = f"test-m-id-{i}"
        label = f"some station_{i}"
        coord = (1.0 + 5.1*i, 4.0 - 4.9*i)
        trange = (10+i, -5+0.5*i)
        river = f"River {i}"
        town = f"My Town {i}"
        s = MonitoringStation(station_id, measure_id, label, coord, trange, river, town)
        lst.append(s)

    for i in range(5,10):
        station_id = f"{i}"
        measure_id = f"test-m-id-{i}"
        label = f"some station_{i}"
        coord = (4.0 - 4.9*i, 1.0 + 5.1*i)
        trange = (1.0+0.01*i, 9+i)
        river = f"River {i}"
        town = f"My Town {i}"
        s = MonitoringStation(station_id, measure_id, label, coord, trange, river, town)
        lst.append(s)

    counter = 0
    for i in inconsistent_typical_range_stations(lst):
        assert int(i.station_id) == counter
        counter += 1

test_inconsistent_typical_range_stations()
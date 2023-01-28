# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data."""

from haversine import haversine # To calculate distance on sphere given coordinates
from utils import sorted_by_key  # noqa -> no quality assurance. 
'''Adding # noqa to a line indicates that the linter (a program that automatically 
checks code quality) should not check this line. Any warnings that code may have 
generated will be ignored.'''


def stations_by_distance(stations:list, p:tuple) -> list:
    """Takes a list of station objects and a coordinate p (tuple), 
    and returns a list of (station, distance) tuples, where distance (float) is 
    the distance of the station (MonitoringStation) from the coordinate p"""

    lst = []     # The list to be returned
    for station in stations:
        distance = haversine(station.coord, p)
        lst.append((station.name, distance))

    return sorted_by_key(lst, 1)   # Sorts list according to distance

def rivers_with_station(stations):
    """given a list of station objects, returns a container (list/tuple/set) 
    with the names of the rivers with a monitoring station. """

    river = set()
    for station in stations:
        river.add(station.river)

    return river

def stations_by_river(stations):
    """implement a function that returns a Python dict (dictionary) that maps river names (the ‘key’) to a list of station objects on a given river."""

    dict = {}
    for station in stations:
        common = set()
        for station2 in stations:
            if station2.river ==  station.river and station2.name != station.name:
                common.add(station2.name)
        dict[station.river] = common
    
    return dict

def stations_within_radius(stations: list, centre: tuple, r: float or int) -> list:
    """A function that returns a list of all stations (type MonitoringStation) 
    within radius r of a geographic coordinate.

    [stations] is a list of MonitoringStation objects, 
    [centre] is the coordinate x
    [r] is the radius."""

    lst = []
    fr = float(r)
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance <= fr:
            lst.append(station)
    return lst



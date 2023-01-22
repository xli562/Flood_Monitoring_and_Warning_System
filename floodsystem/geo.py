# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data."""

from haversine import haversine # To calculate distance on sphere given coordinates
from .utils import sorted_by_key  # noqa -> no quality assurance. 
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
        lst.append((station.name, station.town, distance))

    return sorted_by_key(lst, 2)   # Sorts list according to distance


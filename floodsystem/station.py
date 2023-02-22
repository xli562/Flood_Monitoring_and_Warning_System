# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station

    In a submodule station, create a class MonitoringStation that 
    represents a monitoring station, and has attributes:
    Station ID (string)
    Measurement ID (string)
    Name (string)
    Geographic coordinate (tuple(float, float))
    Typical low/high levels (tuple(float, float))
    River on which the station is located (string)
    Closest town to the station (string)
    """

    def __init__(self, station_id: str, measure_id: str, label: str, coord: tuple, 
                typical_range: tuple, river: str, town: str):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
    
    def __repr__(self) -> str:
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self) -> bool:
        """Returns True if data is consistent and False if the data is inconsistant or unavailable."""
        consistancy = False
        if self.typical_range != None: 
            if self.typical_range[0] < self.typical_range[1]:
                consistancy = True
        return consistancy

    def relative_water_level(self) -> float or None:
        """returns the latest water level as a fraction of the typical range, 
        i.e. a ratio of 1.0 corresponds to a level at the typical high 
        and a ratio of 0.0 corresponds to a level at the typical low. 
        If the necessary data is not available or is inconsistent, 
        the function should return None."""

        rlevel = None      # rlevel = relative water level
        trange = self.typical_range
        llevel = self.latest_level

        if trange != None and llevel != None:
            rlevel = (llevel - trange[0]) / (trange[1] - trange[0])
        
        return rlevel



def inconsistent_typical_range_stations(stations) -> list:
    """A function that, given a list of station objects, returns a list of stations that have inconsistent data. """

    inconsistant_list = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistant_list.append(station)
    return inconsistant_list


def create_stations_list_for_testing() -> list:
    """Creates a list of 5 stations for testing.
    
    An example of an element:
    Station name:     some station_1
    id:            1
    measure id:    test-m-id-1
    coordinate:    (6.1, -0.9000000000000004)
    town:          My Town 1
    river:         River 1
    typical range: (-1.911126544120213, 3.8704108757126026)

    latest level:  1.4586000733679922"""

    from random import random
    lst = []
    for i in range(5):
            station_id = f"{i}"
            measure_id = f"test-m-id-{i}"
            label = f"some station_{i}"
            coord = (1.0 + 5.1*i, 4.0 - 4.9*i)
            trange = (-2.3 + random(), 3.4445 + random())
            river = f"River {i}"
            town = f"My Town {i}"
            s = MonitoringStation(station_id, measure_id, label, coord, trange, river, town)
            if i == 4:
                s.latest_level = trange[1] * 2    # Making sure at least one station exceeds the typical range
            else:
                s.latest_level = ((trange[0]+trange[1])/2)+random()*(trange[1]-trange[0])
            lst.append(s)

    return lst
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

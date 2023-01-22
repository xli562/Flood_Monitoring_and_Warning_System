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

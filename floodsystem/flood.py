from .stationdata import update_water_levels
from utils import sorted_by_key

def stations_level_over_threshold(stations, tol) -> list:
    '''Stations is a list of MonitoringStation objects. 
    Consider only stations with consistent typical low/high data.
    
    a function that returns a list of tuples, where 
    each tuple holds (i) a station (object) at which 
    the latest relative water level is over tol and 
    (ii) the relative water level at the station. The returned 
    list should be sorted by the relative level in descending order.'''

    lst = []

    for station in stations:
        rlevel = station.relative_water_level()     # rlevel = relative water level
        if rlevel != None:
            if rlevel > tol:
                lst.append((station, rlevel))

    return sorted_by_key(lst, 1)

def stations_highest_rel_level(stations: list, N: int) -> list:
    """Remember to update water level of the stations before calling this function!
    
    Takes a list of MonitoringStation objects.
    Returns a list of the N stations (objects) at which the 
    relative water level is highest.
    The list is sorted in descending order by relative level."""
    stRlevel = []    # list of (Station, relative level) tuples
    lst = []         # The final list to be outputted
    for station in stations:
        rlevel = station.relative_water_level()
        if rlevel != None:
            stRlevel.append((station, rlevel))

    stRlevel = sorted_by_key(stRlevel, 1, reverse=True)
    stRlevel = stRlevel[:N]
    for tup in stRlevel:
        lst.append(tup[0])

    return lst
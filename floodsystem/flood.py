from .stationdata import build_station_list, update_water_levels
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





from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Builds a list of all stations with inconsistent typical range data. 
    Prints a list of station names, in alphabetical order, for stations with inconsistent data."""
    lst = []
    # inconStations = inconsistent stations
    inconStations = inconsistent_typical_range_stations(build_station_list())
    for inconStation in inconStations:
        lst.append(inconStation.name)
    lst.sort()
    print(lst)



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()


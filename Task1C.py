from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Provide a program file Task1C.py that uses the function geo.stations_within_radius 
    to build a list of stations within 10 km of the Cambridge city centre 
    (coordinate (52.2053, 0.1218)). Print the names of the stations, 
    listed in alphabetical order."""
    ctr = (52.2053, 0.1218)
    r = 10
    stations = build_station_list()
    lstOfSt = stations_within_radius(stations, ctr, r)  #list of Station entities
    lst = []
    for i in lstOfSt:
        lst.append(i.name)
    lst.sort()
    print(lst)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
    
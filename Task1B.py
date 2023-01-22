from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    """Provide a program file Task1B.py that uses geo.stations_by_distance 
    and prints a list of tuples (station name, town, distance) for the 10 
    closest and the 10 furthest stations from the Cambridge city centre, 
    (52.2053, 0.1218). """

    stations = build_station_list()
    print(f'Closest 10 stations: \n    {stations_by_distance(stations, (52.2053, 0.1218))[:10]}')
    print()
    print(f'Furthest 10 stations: \n    {stations_by_distance(stations, (52.2053, 0.1218))[-10:]}')


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
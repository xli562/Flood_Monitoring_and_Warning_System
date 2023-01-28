from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def run():
    """Provide a program file Task1B.py that uses geo.stations_by_distance 
    and prints a list of tuples (station name, town, distance) for the 10 
    closest and the 10 furthest stations from the Cambridge city centre, 
    (52.2053, 0.1218). """

    lstOfStations = build_station_list() # The list of all station entities
    # The lists to be outputted
    outFirst10 = []
    outLast10 = []
    # Tuple of first 10 stations in (station, distance) format
    first10 = stations_by_distance(lstOfStations, (52.2053, 0.1218))[:10]
    # Tuple of flast 10 stations in (station, distance) format
    last10 = stations_by_distance(lstOfStations, (52.2053, 0.1218))[-10:]
    for i in lstOfStations:
        for fs in first10:
            if i.name == fs[0]:
                outFirst10.append((fs[0], i.town, fs[1]))
        for ls in last10:
            if i.name == ls[0]:
                outLast10.append((ls[0], i.town, ls[1]))
    
    print(f'Closest 10 stations: \n    {sorted_by_key(outFirst10, 2)}')
    print()
    print(f'Furthest 10 stations: \n    {sorted_by_key(outLast10, 2)}')


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
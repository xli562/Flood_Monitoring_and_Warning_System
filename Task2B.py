from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    stations = build_station_list()
    update_water_levels(stations)
    lst = stations_level_over_threshold(stations, 0.8)
    for tup in lst:
        name = tup[0].name
        rlevel = tup[1]
        print(name, rlevel)


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
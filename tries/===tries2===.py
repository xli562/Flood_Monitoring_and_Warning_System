from floodsystem.stationdata import build_station_list

stations = build_station_list()
print(stations)
for station in stations:
    if station.name == 'Cam':
        print(station.measure_id)
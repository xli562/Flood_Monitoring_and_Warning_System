from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

print(len(rivers_with_station(build_station_list())))
m = sorted(rivers_with_station(build_station_list())) # sort the set
print(m[0:10]) # first 10 stations sorted

n = stations_by_river(build_station_list()) # the whole dictionary
print("Stations on River Aire are", n["River Aire"])
print("Stations on River Cam are", n["River Cam"])
print("Stations on River Thames are", n["River Thames"])
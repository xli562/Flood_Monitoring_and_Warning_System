from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

print(rivers_by_station_number(build_station_list(), 9))

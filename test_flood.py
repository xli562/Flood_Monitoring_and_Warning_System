from floodsystem.station import create_stations_list_for_testing
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    stations = create_stations_list_for_testing()
    lst = stations_level_over_threshold(stations, 1)
    assert len(lst) > 0
    print('PASSED test_stations_level_over_threshold')

def test_stations_highest_rel_level():
    stations = create_stations_list_for_testing()
    highests = stations_highest_rel_level(stations, 3)
    assert len(highests) == 3
    assert highests[0].relative_water_level() >= highests[1].relative_water_level() and highests[1].relative_water_level() > highests[2].relative_water_level()
    print('PASSED test_stations_highest_rel_level')

test_stations_highest_rel_level()
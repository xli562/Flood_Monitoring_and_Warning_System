from floodsystem.station import create_stations_list_for_testing
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():
    stations = create_stations_list_for_testing()
    lst = stations_level_over_threshold(stations, 1)
    assert len(lst) > 0
    print('PASSED test_stations_level_over_threshold')
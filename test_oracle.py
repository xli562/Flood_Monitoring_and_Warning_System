from floodsystem.oracle import predict
from floodsystem.stationdata import build_station_list

def test_predict():
    stationsCount = 3
    a = predict(build_station_list(), pastDays=2, futureDays = 1, stationsCount=3, usePrevExcel=False, seasonal=True)
    assert type(a) == dict
    assert len(a) == 3
    assert type(a.values()[0]) == list
    assert type(a.keys()[0]) == str
    # making sure the lists are not all 'none's.
    counter = 0
    for i in a.values()[0]:
        if i == None:
            counter += 1
    assert counter < 0.5*len(a.values()[0])
    print('PASSED test_predict')
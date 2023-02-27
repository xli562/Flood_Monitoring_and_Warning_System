from floodsystem.oracle import predict
from floodsystem.stationdata import build_station_list

a = predict(build_station_list(), pastDays=2, futureDays = 1, stationsCount=2, usePrevExcel=False, seasonal=True)
print(a)

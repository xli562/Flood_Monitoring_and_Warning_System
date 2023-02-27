from floodsystem.oracle import predict
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import build_station_list, update_water_levels

a = predict(build_station_list(), pastDays=2, futureDays = 1, stationsCount=3, usePrevExcel=True, seasonal=True)

testation = list(a.keys())
testlevel = list(a.values())

stations = build_station_list()
update_water_levels(stations)

for i in range(len(testation)):
    for station in stations:
        if station.name == testation[i]:
            typhigh = station.typical_range[1]
            level = testlevel[i]
            for j in range(len(level)):
                ty = level[j]
                length = int(len(level))
                if level[j] != "#NAME?":
                    p = 0
                    if ty >= 15000*typhigh:
                        if ty >= 20000*typhigh:
                            if ty >= 30000*typhigh:
                                print("{} is at severe risk for the next day.".format(testation[i]))
                                break
                            else:
                                print("{} is at high risk for the next day.".format(testation[i]))
                                break
                        else:
                            print("{} is at moderate risk for the next day.".format(testation[i]))
                            break
                    else:
                        p += 1
                        if p >= length/2 - 1:
                            print("{} is at low risk for the next day.".format(testation[i]))
                            break

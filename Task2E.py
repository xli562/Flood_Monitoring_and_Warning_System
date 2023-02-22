from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_latest_water_level_data
from floodsystem.datafetcher import fetch_measure_levels
import datetime

#Define a function that finds the top x stations with highest water level
def top_water_level(x):

    data = fetch_latest_water_level_data()
    items = data['items']
    rank = []

    #getting the data
    for w in items:
        m = dict(w)
        #pick out all valid data because this stupid library contains useless info that cost me two hours wondering why the key wont work and the meaning of my life
        measures = m.get('latestReading')
        if measures != None:
            value = measures['value']
            if type(value) == float:
                rank.append((w["@id"], value, w["label"]))
    
    #sorting the data
    sort = sorted(rank, key=lambda x: x[1], reverse = True)
    return sort[:x]

#Fetch the data for those stations
station1 = top_water_level(5)[0]
station2 = top_water_level(5)[1]
station3 = top_water_level(5)[2]
station4 = top_water_level(5)[3]
station5 = top_water_level(5)[4]
allstations = [station1, station2, station3, station4, station5]

label = []
time = []
level = []
for i in allstations:
    label.append(i[2])
    fetch = fetch_measure_levels(i[0], datetime.timedelta(10))
    time.append(fetch[0])
    level.append(fetch[1])

plot_water_levels(label, time, level, share = False)
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_latest_water_level_data
from floodsystem.datafetcher import fetch_measure_levels
import datetime

#Define a function that finds the top x stations with highest water level
def top_water_level(x):
    "Searching for the  top x stations with highest water level"
    data = fetch_latest_water_level_data()
    items = data['items']
    rank = []

    #getting the data
    for w in items:
        m = dict(w)
        
        measures = m.get('latestReading')
        if measures != None:
            value = measures['value']
            if type(value) == float:
                rank.append((w["@id"], value, w["label"]))
    
    #sorting the data
    sort = sorted(rank, key=lambda x: x[1], reverse = True)
    return sort[:x]

#Get the top stations
station1 = top_water_level(5)[0]
station2 = top_water_level(5)[1]
station3 = top_water_level(5)[2]
station4 = top_water_level(5)[3]
station5 = top_water_level(5)[4]
allstations = [station1, station2, station3, station4, station5]

#Fetch the data for top 5 stations with greatest real-time water level, using function created in Task2E
for i in allstations:
    label = i[2]
    fetch = fetch_measure_levels(i[0], datetime.timedelta(2))
    time = fetch[0]
    level = fetch[1]
    plot_water_level_with_fit(label, time, level, 4)

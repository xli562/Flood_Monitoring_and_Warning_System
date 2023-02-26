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






from floodsystem.datafetcher import fetch_measure_levels
import pmdarima as pm
from pmdarima import model_selection
import numpy as np
import datetime
from datetime import timedelta
from matplotlib import pyplot as plt


fetch = fetch_measure_levels(station5[0], datetime.timedelta(365))

data = np.asarray(fetch[1])


train, test = model_selection.train_test_split(data, train_size=0.5)

arima_model = pm.auto_arima(train, error_action='ignore', trace=True,
                      suppress_warnings=True, maxiter=10,
                      seasonal=True, m=12)
#automatically fit the optimal ARIMA model for given time series
arima_model_fitted = pm.auto_arima(data)
# one-step out-of sample forecast
forecast = arima_model.predict(n_periods=len(data))

x = np.arange(test.shape[0])
plt.plot(x, test)
plt.plot(np.arange(forecast.shape[0]), forecast)
plt.title('Actual test samples vs. forecasts')
plt.show()
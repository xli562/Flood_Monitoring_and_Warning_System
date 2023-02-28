from floodsystem.datafetcher import fetch_measure_levels
import pmdarima as pm
from pmdarima import model_selection
import numpy as np
import datetime
from matplotlib import pyplot as plt

def mapping(inlst: list, lout: int, hout: int) -> list | int:
    """ Takes inlst [the INput LiST] and compresses it to have length as close to lout [Length of OUTput] as possible, 
    and times all elements by hout [Hight of OUTput.]"""
    outlst = [] # the list to be outputted
    length = len(inlst)
    if lout == 0:
        lout = length
    step = int(length / lout)
    for i in range(lout):
        outlst.append(inlst[i]*hout)
    return outlst

measure_id = 'http://environment.data.gov.uk/flood-monitoring/id/measures/E79000-level-stage-i-15_min-m'
dt = datetime.timedelta(5)
histLvAndTime = fetch_measure_levels(measure_id, dt)
data = np.asarray(histLvAndTime[1])
data = np.asarray(mapping(data,len(data), 50000))

#data = pm.datasets.load_wineind()

train, test = model_selection.train_test_split(data, train_size=0.5)
# Fit a simple auto_arima model
arima_model = pm.auto_arima(train, error_action='ignore', trace=True,
                    suppress_warnings=True, maxiter=5,
                    seasonal=False, m=1)

forecast = arima_model.predict(n_periods=test.shape[0])
# Plot actual test vs. forecasts:
xtest = np.arange(len(test))
xpredict = np.arange(len(forecast)-1, 2*len(forecast)-1)

plt.plot(xtest, test)
plt.plot(xpredict, forecast)
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.title(f'Actual test samples vs. forecasts (m = {7})')
plt.show()



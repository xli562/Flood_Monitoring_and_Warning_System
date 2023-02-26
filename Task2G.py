from floodsystem.datafetcher import fetch_measure_levels
import pmdarima as pm
from pmdarima import model_selection
import numpy as np
import datetime
from datetime import timedelta
from matplotlib import pyplot as plt

def data(stations: list, days: timedelta) -> list:
    """Takes a list of MonitoringStation objects
    and the time range interested in the datetime.timedelta form.
    
    Outputs a list of 3-element tuples:
    (Name of station: str, 
    historic relative water level readings: list, 
    the days on which the recordings were made: list)"""

def sarima_predict()

measure_id = 'http://environment.data.gov.uk/flood-monitoring/id/measures/2514-level-stage-i-15_min-mASD'
dt = datetime.timedelta(365)
data = np.asarray(fetch_measure_levels(measure_id, dt)[1])


train, test = model_selection.train_test_split(data, train_size=0.7)

arima_model = pm.auto_arima(train, error_action='ignore', trace=True,
                      suppress_warnings=True, maxiter=10,
                      seasonal=True, m=20)
#automatically fit the optimal ARIMA model for given time series
arima_model_fitted = pm.auto_arima(data)
# one-step out-of sample forecast
forecast = arima_model.predict(n_periods=100)

x = np.arange(test.shape[0])
plt.plot(x, test)
plt.plot(np.arange(forecast.shape[0]), forecast)
plt.title('Actual test samples vs. forecasts')
plt.show()
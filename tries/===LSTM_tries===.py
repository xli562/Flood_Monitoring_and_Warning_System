from floodsystem.stationdata import build_station_list

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
"""We will use MinMaxScaler class from the 
sklear.preprocessing library to scale our data between 0 and 1. 
The feature_range parameter is used to specify the range of the scaled data."""

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

# ======= Import Dataset =======
stations = build_station_list()

apple_training_processed = []
for i in range(1,137):
    apple_training_processed.append(i)

# ======= Data Normalization =======
scaler = MinMaxScaler(feature_range = (0, 1))
apple_training_scaled = scaler.fit_transform(apple_training_processed)

# ======= Convert Training Data to Right Shape =======
features_set = []
labels = []
for i in range(6, 126):
    features_set.append(apple_training_scaled[i-6:i])
    labels.append(apple_training_scaled[i])
features_set = np.array(features_set)
labels = np.array(labels)

features_set = np.reshape(features_set, (features_set.shape[0], features_set.shape[1], 1))
print(features_set)
print(labels)

# ======= Training The LSTM =======
model = Sequential()

# ======= Creating LSTM and Dropout Layers =======
model.add(LSTM(units=50, return_sequences=True, input_shape=(features_set.shape[1], 1)))
model.add(Dropout(0.2))

model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50))
model.add(Dropout(0.2))

# ======= Creating Dense Layer =======
model.add(Dense(units = 1))

# ======= Model Compilation =======
model.compile(optimizer = 'adam', loss = 'mean_squared_error')

# ======= Algorithm Training =======
model.fit(features_set, labels, epochs = 100, batch_size = 32)
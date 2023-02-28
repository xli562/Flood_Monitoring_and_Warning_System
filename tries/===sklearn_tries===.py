from sklearn.linear_model import PassiveAggressiveRegressor 

measure_id = 'http://environment.data.gov.uk/flood-monitoring/id/measures/E79000-level-stage-i-15_min-m'
dt = datetime.timedelta(1)
histLvAndTime = fetch_measure_levels(measure_id, dt)
y = np.asarray(histLvAndTime[1])

model = LinearRegression()
model.fit(x_train, y_train) # Fitting on Training Data
model.predict(20) #One value in test data is 20
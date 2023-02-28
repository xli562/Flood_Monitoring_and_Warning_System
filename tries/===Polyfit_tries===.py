from floodsystem.datafetcher import fetch_measure_levels
import datetime

import numpy as np
import matplotlib.pyplot as plt

# Create set of 10 data points on interval (0, 2)
measure_id = 'http://environment.data.gov.uk/flood-monitoring/id/measures/2514-level-stage-i-15_min-mASD'
dt = datetime.timedelta(365)
histLvAndTime = fetch_measure_levels(measure_id, dt)
y = np.asarray(histLvAndTime[1])

for i in y:
    print(i)

assert 0

x = np.linspace(0, 2, len(y))

# Find coefficients of best-fit polynomial f(x) of degree 4
p_coeff = np.polyfit(x, y, 150)

# Convert coefficient into a polynomial that can be evaluated,
# e.g. poly(0.3)
poly = np.poly1d(p_coeff)

# Plot original data points
plt.plot(x, y, '.')

# Plot polynomial fit at 30 points along interval
x1 = np.linspace(x[0], x[-1], 30)
plt.plot(x1, poly(x1))

# Display plot
plt.show()
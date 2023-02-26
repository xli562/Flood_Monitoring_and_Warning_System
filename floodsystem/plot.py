from matplotlib import pyplot as plt
from matplotlib import dates as dat
import numpy as np
from analysis import polyfit
from .station import MonitoringStation

def plot_water_levels(station: MonitoringStation, dates, levels, sharey = True) -> None:
    "Plot the water level vs. date graph of no more than 6 stations"

    if len(dates) > 6 or len(station) > 6 or len(levels) > 6:
        print("Too many stations.")

    # Checking data consistency
    if len(dates) != len(levels) or len(station) != len(levels) or len(dates) != len(station):
        print("Number of stations do not match number of dates/levels.")

    fig, sub = plt.subplots(len(station), sharex=True, sharey = sharey)
    fig.suptitle(f"Water levels over past 10 days for top {len(station)} stations with greatest current relative water level")
    
    n = 0
    for n in range(len(station)):
        sub[n].plot(dates[n],levels[n])
        sub[n].set_title(station[n])
        sub[n].set_ylabel('water level (m)')
        ymax = max(levels[n])
        xpos = levels[n].index(ymax)
        daten = dates[n]
        xmax = daten[xpos]
        sub[n].annotate('max={}'.format(ymax), xy=(xmax, ymax), xytext=(xmax, ymax),
            arrowprops=dict(facecolor='black', shrink=0.01),
            )
        ymin = min(levels[n])
        xpos1 = levels[n].index(ymin)
        xmin = daten[xpos1]
        sub[n].annotate('min={}'.format(ymin), xy=(xmin, ymin), xytext=(xmin, ymin),
            arrowprops=dict(facecolor='black', shrink=0.01),
            )
        n = n + 1

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.xticks(rotation=45)

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    "plot the best-fit polynomial of p degrees for one station's water level vs. date graph"
    plt.plot(dates, levels, '.')

    poly = polyfit(dates, levels, p)

    # Plot polynomial fit at 50 points along interval
    ndate = dat.date2num(dates)
    shift = np.linspace(ndate[0], ndate[-1], 50)
    plt.plot(shift, poly(shift - shift[0]))
    funct = list(poly(shift - shift[0]))
    ymax = max(poly(shift - shift[0]))
    xpos = funct.index(ymax)
    xmax = shift[xpos]
    plt.annotate('max={}'.format(ymax), xy=(xmax, ymax), xytext=(xmax, ymax),
        arrowprops=dict(facecolor='black', shrink=0.01),
        )
    ymin = min(poly(shift - shift[0]))
    xpos1 = funct.index(ymin)
    xmin = shift[xpos1]
    plt.annotate('min={}'.format(ymin), xy=(xmin, ymin), xytext=(xmin, ymin),
        arrowprops=dict(facecolor='black', shrink=0.01),
        )
    
    plt.title(label='Best-fit polynomial for {}'.format(station))

    # Display plot
    plt.show()
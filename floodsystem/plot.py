from matplotlib import pyplot as plt

def plot_water_levels(station, dates, levels, share = True):

    if len(dates) > 6 or len(station) > 6 or len(levels) > 6:
        return(print("Too many stations."))

    
    if len(dates) != len(levels) or len(station) != len(levels) or len(dates) != len(station):
        return(print("Number of stations do not match number of dates/levels."))

    fig, sub = plt.subplots(len(station), sharex=True, sharey = share)
    fig.suptitle("Water levels over past 10 days for top {} stations with greatest current relative water level".format(len(station)))
    
    n = 0
    for n in range(len(station)):
        sub[n].plot(dates[n],levels[n])
        sub[n].set_title(station[n])
        sub[n].set_ylabel('water level (m)')
        n = n + 1

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.xticks(rotation=45);

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
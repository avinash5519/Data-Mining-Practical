import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# For plotting
mapdata = np.loadtxt("../input_data/mapdata_copyright_openstreetmap_contributors.txt")
lon_lat_box = (-88, -87.5, 41.6, 42.1)

# Relevant data collected from all the traps
observations = pd.read_csv('../input_data/train.csv', parse_dates=['Date'])[['Date', 'Trap','Longitude', 'Latitude', 'WnvPresent']]

# Locations of all unique traps
unique_traps = observations[['Trap', 'Longitude', 'Latitude']].drop_duplicates().values

trap_locations = {trap: [longitude, latitude] for (trap, longitude, latitude) in unique_traps}
traps = trap_locations.keys()

years = [2007, 2009, 2011, 2013]

# The week numbers of the earlist and latest measurements across the dataset
start_week = 21
end_week = 41

for year in years:
    # Select observations of the given year
    obs_year = observations[observations['Date'].apply(lambda x: x.year) == year]
    for week in range(start_week, end_week):
        # Select observations of the given week
        obs_week = obs_year[obs_year['Date'].apply(lambda x: x.week) == week]
        # Extract locations of infected and non-infected traps
        infected = obs_week[obs_week['WnvPresent'] == 1][['Longitude', 'Latitude']]
        non_infected = obs_week[obs_week['WnvPresent'] == 0][['Longitude', 'Latitude']]

        plt.figure(figsize=(5, 5))
        plt.title("Year %d, week %d" % (year, week))
        plt.imshow(mapdata, extent=lon_lat_box, cmap=plt.get_cmap('gray'))
        plt.scatter(unique_traps[:,1], unique_traps[:,2],
            marker='x', s=10, c=u'g', label='Traps not collected this week')
        if not non_infected.empty:
            plt.scatter(non_infected.values[:,0], non_infected.values[:,1],
            marker='x', s=20, c=u'b', label='Collected traps with no WNV')
        if not infected.empty:
            plt.scatter(infected.values[:,0], infected.values[:,1],
            marker='x', s=20, c=u'r', label='Collected traps with WNV')

        plt.savefig('../plots/traps_by_week/%d/%d.png' % (year, week))
        print("Year %d, week %d saved" % (year, week))
        plt.close()

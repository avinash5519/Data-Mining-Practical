#The original script has been released under the Apache 2.0 open source license
#http://www.apache.org/licenses/LICENSE-2.0
#author - https://www.kaggle.com/users/213536/vasco

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
#%matplotlib inline

from sklearn.neighbors import KernelDensity

mapdata = np.loadtxt("../input_data/mapdata_copyright_openstreetmap_contributors.txt")
traps = pd.read_csv('../input_data/train.csv', parse_dates=['Date'])[['Date', 'Trap','Longitude', 'Latitude', 'WnvPresent']]

alpha_cm = plt.cm.Reds
alpha_cm._init()
alpha_cm._lut[:-3,-1] = abs(np.logspace(0, 1, alpha_cm.N) / 10 - 1)[::-1]
aspect = mapdata.shape[0] * 1.0 / mapdata.shape[1]
lon_lat_box = (-88, -87.5, 41.6, 42.1)


for year, subplot in zip([2007, 2009, 2011, 2013], [141, 142, 143, 144]):
    plt.figure()
    sightings = traps[(traps['WnvPresent'] > 0) & (traps['Date'].apply(lambda x: x.year) == year)]
    sightings = sightings.groupby(['Date', 'Trap','Longitude', 'Latitude']).max()['WnvPresent'].reset_index()
    X = sightings[['Longitude', 'Latitude']].values
    kd = KernelDensity(bandwidth=0.02)
    kd.fit(X)

    xv,yv = np.meshgrid(np.linspace(-88, -87.5, 100), np.linspace(41.6, 42.1, 100))
    gridpoints = np.array([xv.ravel(),yv.ravel()]).T
    zv = np.exp(kd.score_samples(gridpoints).reshape(100,100))
    plt.gca().set_title(year)
    plt.imshow(mapdata,
               cmap=plt.get_cmap('gray'),
               extent=lon_lat_box)
    plt.imshow(zv,
               origin='lower',
               cmap=alpha_cm,
               extent=lon_lat_box)
    locations = traps[['Longitude', 'Latitude']].drop_duplicates().values
    plt.scatter(locations[:,0], locations[:,1], marker='x')

    plt.savefig('../plots/heatmap_%d.png' % year, transparent=True)

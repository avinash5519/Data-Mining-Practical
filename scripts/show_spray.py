import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mapdata = np.loadtxt("../input_data/mapdata_copyright_openstreetmap_contributors.txt")

spray = pd.read_csv('../input_data/spray/spray2013.csv')[['Longitude', 'Latitude']].values
lon_lat_box = (-88, -87.5, 41.6, 42.1)

plt.figure(figsize=(12., 12.))
plt.gca().set_title('Spray sites in 2013')
plt.imshow(mapdata, extent=lon_lat_box, cmap=plt.get_cmap('gray'))
plt.scatter(spray[:,0], spray[:,1], s=5, marker='o', c='red', edgecolors='none', alpha=0.1)
plt.savefig('../plots/spray_2013.png', transparent=True)




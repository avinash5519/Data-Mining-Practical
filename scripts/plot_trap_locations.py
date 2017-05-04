import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mapdata = np.loadtxt("../input_data/mapdata_copyright_openstreetmap_contributors.txt")
traps = pd.read_csv('../input_data/train.csv')[['Longitude', 'Latitude']]

locations = traps.drop_duplicates().values
lon_lat_box = (-88, -87.5, 41.6, 42.1)


plt.figure()
plt.gca().set_title('Trap locations')
plt.imshow(mapdata, extent=lon_lat_box, cmap=plt.get_cmap('gray'))
plt.scatter(locations[:,0], locations[:,1], marker='x')
plt.savefig('../plots/trap_locations.png', transparent=True)

import numpy as np
import matplotlib.pyplot as plt

mapdata = np.loadtxt("../input_data/mapdata_copyright_openstreetmap_contributors.txt")
lon_lat_box = (-88, -87.5, 41.6, 42.1)


plt.figure()
plt.gca().set_title('City of Chicago')
plt.imshow(mapdata, extent=lon_lat_box, cmap=plt.get_cmap('gray'))
plt.savefig('../plots/map.png', transparent=True)

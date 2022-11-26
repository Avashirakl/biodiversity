import pandas as pd
import matplotlib.pyplot as plt

observations = pd.read_csv("../observations.csv")
species = pd.read_csv("../species_info.csv")

merged = observations.merge(species, how='inner', on='scientific_name')

pivot1 = pd.pivot_table(merged, values='observations', index='park_name', columns='category', aggfunc='sum')
ax = pivot1.plot(kind='bar', figsize=(7, 8), stacked=True)
ax.set_title("Statistics on the number of species category in each park")
print(type(ax))

plt.xlabel('Park names', fontsize=15)
plt.ylabel('Number of Species (million)', fontsize=14)
ax1_x = ['Bryce\nNational\nPark',
         'Great\nSmoky\nMountains\nNational\nPark',
         'Yellowstone\nNational\nPark',
         'Yosemite\nNational\nPark']

ax.set_xticklabels(ax1_x)

plt.xticks(rotation='horizontal')
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

observations = pd.read_csv("../observations.csv")
species = pd.read_csv("../species_info.csv")
species.fillna('No Intervention', inplace=True)

merged = observations.merge(species, how='inner', on='scientific_name')

pv = pd.pivot_table(merged[merged.conservation_status != "No Intervention"], aggfunc='sum',
                    index='park_name', columns='conservation_status', values='observations')

labels = ['Bryce\nNational\nPark', 'Great\nSmoky\nMountains\nNational\nPark',
          'Yellowstone\nNational\nPark', 'Yosemite\nNational\nPark']

bar = pv.plot(kind='bar', figsize=(7, 8),
              stacked=True)
bar.set_title("Park observation statistics by conservation status")
bar.set_xticklabels(labels)


plt.xlabel('Park names', fontsize=15)
plt.ylabel('Observation Amount', fontsize=14)
plt.xticks(rotation='horizontal')
plt.tight_layout()
plt.show()


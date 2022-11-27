import pandas as pd
import matplotlib.pyplot as plt

observations = pd.read_csv("../observations.csv")
species = pd.read_csv("../species_info.csv")

merged = observations.merge(species, how='inner', on='scientific_name')

merged.fillna('No intervention', inplace=True)
merged['is_protected'] = merged.conservation_status != 'No intervention'

category_counts = merged.groupby(['category', 'is_protected']).observations.sum().reset_index()

pivot = pd.pivot_table(category_counts, columns='is_protected', index='category', values='observations')

pivot.columns = ['not_protected', 'protected']
colors = ['yellow', '#7eb54e']
ax = pivot.plot(kind='bar', figsize=(7, 8), stacked=False, color=colors)

ax.set_title("Statistics on the amount of observations\nboth on protected and unprotected species by categories\n")

plt.xlabel('Categories', fontsize=15)
plt.ylabel('Amount of observations (million)', fontsize=14)

plt.xticks(rotation='horizontal')
ax1_x = ['Amphibian', 'Bird', 'Fish', 'Mammal', 'Nonvascular\nPlant',
         'Reptile', 'Vascular\nPlant']

ax.set_xticklabels(ax1_x)

plt.show()

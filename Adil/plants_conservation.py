import pandas as pd
import matplotlib.pyplot as plt


observations = pd.read_csv("../observations.csv")
species = pd.read_csv("../species_info.csv")

print(species['conservation_status'].unique())
merged = observations.merge(species, how='inner', on='scientific_name')
df = merged

print(df.columns)
print(df['category'].unique())

df.dropna()
df = df[(df['category'] == 'Vascular Plant') | (df['category'] == 'Nonvascular Plant')]

print(len(df['category']))
print(df['conservation_status'].unique())

p = pd.pivot_table(df, index='conservation_status', columns='category')

a = p.plot(kind='bar', figsize=(7, 8),)

a.set_title("Statistics of the number of plants in each conservation status")

plt.xlabel('Status names', fontsize=15)
plt.ylabel('Number of plants', fontsize=14)

plt.xticks(rotation='horizontal')
plt.tight_layout()
plt.show()

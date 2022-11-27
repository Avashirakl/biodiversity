import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

observations = pd.read_csv("../observations.csv")
species = pd.read_csv("../species_info.csv")

merged = observations.merge(species, how='inner', on='scientific_name')  # merged 2 csv files

pivot1 = pd.pivot_table(merged, values='observations',
                        index='park_name', columns='category', aggfunc='sum')  # created new pivot

pivot2 = pivot1.idxmax(axis="columns")  # find max category in 1 park

df = pd.DataFrame(pivot2)
df.columns = ['Most of all categories in park']
df = df.rename_axis('Park names', axis=0)
print(tabulate(df, headers='keys', tablefmt='psql'))

df2 = pd.DataFrame(pivot1)
figure = df2.plot(y=['Vascular Plant'], figsize=(13, 8))
figure.set_title('Most of all categories in park', fontweight='bold')
figure.set_xlabel('Park names', fontweight='bold')
figure.set_ylabel('Amount of observations', fontweight='bold')
plt.show()

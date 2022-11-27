import pandas as pd
import matplotlib.pyplot as plt


observations = pd.read_csv("../observations.csv")
species = pd.read_csv("../species_info.csv")

print(species['conservation_status'].unique())
merged = observations.merge(species, how='inner', on='scientific_name')
df1 = merged

df1['conservation_status'] = df1['conservation_status'].fillna('No intervention')
df1['protected'] = df1['conservation_status'] != 'No intervention'

category_counts = df1.groupby(['category', 'protected'])\
                        .scientific_name.nunique()\
                        .reset_index()\
                        .pivot(columns='protected',
                                      index='category',
                                      values='scientific_name')\
                        .reset_index()
category_counts.columns = ['category', 'not_protected', 'protected']

print(category_counts)
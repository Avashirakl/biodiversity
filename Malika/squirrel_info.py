import pandas as pd


observations = pd.read_csv("../observations.csv")
species = pd.read_csv("../species_info.csv")

merged = observations.merge(species, how='inner', on='scientific_name')


merged['is_squirrel'] = merged[merged.category == "Mammal"].common_names.str.contains(r"\Squirrel\b", regex=True)
merged.is_squirrel.fillna(False, inplace=True)
merged.conservation_status.fillna('No intervention', inplace=True)

merged['Total'] = merged.groupby('scientific_name')['observations'].transform('sum')

new_df = merged[merged.is_squirrel].drop_duplicates(subset=['scientific_name']).reset_index(drop=True)
del new_df['observations']
del new_df['category']
del new_df['scientific_name']
del new_df['is_squirrel']

new_df.columns = ['Squirrel Name', 'Park Name', 'Conservation Status', 'Total Observations']

print('{: ^60}Squirrel species information'.format(''))
print('{:_^153}'.format(''))
print(new_df.iloc[:, [1, 0, 2, 3]].to_markdown())

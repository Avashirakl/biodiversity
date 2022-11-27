import pandas as pd

species = pd.read_csv("../species_info.csv")

amphibians = species[species.category == 'Amphibian']['common_names'].reset_index(drop=True)
birds = species[species.category == 'Bird']['common_names'].reset_index(drop=True)
fishes = species[species.category == 'Fish']['common_names'].reset_index(drop=True)
mammals = species[species.category == 'Mammal']['common_names'].reset_index(drop=True)
nonvascular_plants = species[species.category == 'Nonvascular Plant']['common_names'].reset_index(drop=True)
reptiles = species[species.category == 'Reptile']['common_names'].reset_index(drop=True)
vascular_plants = species[species.category == 'Vascular Plant']['common_names'].reset_index(drop=True)

df = pd.concat([amphibians, birds, fishes, mammals, nonvascular_plants, reptiles, vascular_plants], axis=1)

df.columns = ['Amphibian', 'Bird', 'Fish', 'Mammal', 'Nonvascular Plant', 'Reptile', 'Vascular Plant']

print(df)

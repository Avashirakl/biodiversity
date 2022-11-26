import pandas as pd
import string


def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text


species = pd.read_csv("../species_info.csv")

scientific_Names = species.scientific_name.apply(remove_punctuations).str.split().tolist()

cleanRows = []
genus_counted = []

for i in scientific_Names:
    cleanRows.append(i[0])


for i in cleanRows:
    x = cleanRows.count(i)
    genus_counted.append((i, x))

result = pd.DataFrame(set(genus_counted), columns=['Genus', 'Count']).sort_values("Count", ascending=False)\
    .reset_index(drop=True)

print(result)

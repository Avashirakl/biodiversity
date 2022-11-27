import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

observations = pd.read_csv("../observations.csv")
merged = pd.read_csv("../species_info.csv")
merged = observations.merge(merged, how='inner', on='scientific_name')

plt.style.use('ggplot')

plt.title('Number of animals for each category')

plt.hist(merged['category'], edgecolor='black', bins=20, label='Category')

plt.legend(loc='upper right')

plt.xlabel('Category')
plt.ylabel('Number od animals')

plt.tight_layout()

plt.show()
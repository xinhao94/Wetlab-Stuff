# Plot a heatmap using 96-well plate data

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df0 = pd.read_csv('MIC_0.5.csv')
df1 = pd.read_csv('MIC_1.csv')
df2 = pd.read_csv('MIC_2.csv')

# Reverse the default color scheme to make the figure more intuitive
# i.e. higher OD, darker color 
r_cmap = sns.cm.rocket_r

# fig, (ax0, ax1, ax2) = plt.subplots(1,3)

# sns.heatmap(df0, ax = ax0)
# sns.heatmap(df1, ax = ax1)
# sns.heatmap(df2, ax = ax2)

# plt.show()

sns.heatmap(df1, cmap=r_cmap)

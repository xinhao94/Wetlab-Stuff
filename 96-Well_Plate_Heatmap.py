# Plot a heatmap using 96-well plate data

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dfA = pd.read_csv('P1E2-A.csv')
dfB = pd.read_csv('P1E2-B.csv')
dfC = pd.read_csv('P1E2-C.csv')

# Revers the default color scheme to make the figure more intuitive
# i.e. higher OD, darker color 
r_cmap = sns.cm.rocket_r

# fig, (ax0, ax1, ax2) = plt.subplots(1,3)

# sns.heatmap(df0, ax = ax0)
# sns.heatmap(df1, ax = ax1)
# sns.heatmap(df2, ax = ax2)

# plt.show()

# sns.heatmap(df1, cmap=r_cmap)

# Fix the upper limit of color map to compare multiple figures
sns.heatmap(dfC, cmap=r_cmap, vmax=0.5)

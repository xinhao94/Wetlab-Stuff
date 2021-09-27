# E. coli MB1860 Adaptation curve
import numpy as np
import matplotlib.pyplot as plt

day = np.arange(0,8)
conc = [0,0.03,0.0625,0.09,0.18,0.38,1,4]
MIC = []
for i in range(len(conc)):
  MIC.append(0.0625)

plt.step(day, conc, '-', color='black')
plt.title("E. coli MB1860 to Ertapenem", fontdict={'fontsize':15})
plt.xticks(fontsize=15)
plt.xlabel("Elapse time (day)", fontdict={'fontsize':15})
plt.yscale("linear")
plt.yticks(fontsize=15)
plt.ylabel("ETP conc. (mg/L)", fontdict={'fontsize':15})

plt.step(day, MIC, '-', color='red')

plt.figlegend(["Adaptation","MIC"], loc="upper left", bbox_to_anchor=(0.15, 0.9), fontsize=12)
plt.show()

# E. coli MB1860 Adaptation curve
import numpy as np
import matplotlib.pyplot as plt

day = np.arange(0,13)
pop1 = [0,0.03,0.0625,0.09,0.18,0.38,1,4,8,16,16,16,32]
pop2 = [0,0.03,0.0625,0.09,0.18,0.38,1,4,8,16,32,32,32]
pop3 = [0,0.03,0.0625,0.09,0.18,0.38,1,4,8,32,32,32,32]
pop4 = [0,0.03,0.0625,0.09,0.18,0.38,1,4,16,32,32,32,32]
pop5 = [0,0.03,0.0625,0.09,0.18,0.38,1,4,8,16,16,24,32]
pops = [pop1, pop2, pop3, pop4, pop5]
MIC = []
CLSI = []
for i in range(len(pop1)):
  MIC.append(0.0625)

for i in range(len(pop1)):
  CLSI.append(2)

plt.step(day, pop1, '-', color='firebrick')
plt.step(day, pop2, '-', color='greenyellow')
plt.step(day, pop3, '-', color='mediumpurple')
plt.step(day, pop4, '-', color='aqua')
plt.step(day, pop5, '-', color='darkorange')

plt.title("E. coli MB1860 to Ertapenem", fontdict={'fontsize':15})
plt.xticks(fontsize=15)
plt.xlabel("Elapse time (day)", fontdict={'fontsize':15})
plt.yscale("linear")
plt.yticks(fontsize=15)
plt.ylabel("ETP conc. (mg/L)", fontdict={'fontsize':15})

plt.step(day, MIC, '--', color='black')
plt.step(day, CLSI, '-.', color='black')

plt.figlegend(["Pop 1", "Pop 2", "Pop 3", "Pop 4", "Pop 5", "MIC","CLSI BP"], 
              loc="upper left", bbox_to_anchor=(0.12, 0.92), fontsize=12)
plt.show()

# Adaptation rate calculation

import numpy as np
import matplotlib.pyplot as plt

doubling = np.arange(8,13)
iteration = np.arange(1,5)

plt.yscale("log")
plt.grid(True)
plt.xticks(np.arange(min(iteration),max(iteration)+1,1))

rates = []

for d in doubling:
  rate = []
  for i in iteration:
    rate.append(1/pow(2,i*d))
  rates.append(rate)

for rate in rates:
  plt.plot(iteration, rate)

plt.xlabel("Iteration")
plt.ylabel("Min Mutation Rate")
plt.figlegend(doubling, loc="upper right",bbox_to_anchor=(0.9, 0.88))
plt.show()

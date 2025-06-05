import matplotlib.pyplot as plt
import nashpy as nash
import numpy as np

A = np.array([[2, 1], [3, 0]])
game = nash.Game(A)
y0 = np.array([3/5, 2/5])
timepoints = np.linspace(0, 10, 1500)
sharing_population_from_3_over_5, aggressive_population = game.replicator_dynamics(y0=y0, timepoints=timepoints).T
sharing_population_from_2_over_5, aggressive_population = game.replicator_dynamics(y0=y0[::-1], timepoints=timepoints).T
plt.plot(sharing_population_from_3_over_5, color="black")
plt.plot(sharing_population_from_2_over_5, color="black")
plt.ylim(0, 1)
plt.ylabel("Population of sharers over time")
plt.xlabel("Time")
plt.savefig("main.png", dpi=300)

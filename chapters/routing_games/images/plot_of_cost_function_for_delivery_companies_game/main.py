import numpy as np
import matplotlib.pyplot as plt

def C(alpha, beta):
    return alpha ** 3 + 3/2 * beta ** 2 + 2 * alpha * beta + beta ** 2 - 2 * alpha - 2 * beta + 1

# Create grid
alpha_vals = np.linspace(0, 1 / 2, 100)
beta_vals = np.linspace(0, 1 / 2, 100)
alpha, beta = np.meshgrid(alpha_vals, beta_vals)

# Compute Z values
costs = C(alpha, beta)

# Plot heat map
plt.figure(figsize=(8, 6))
cp = plt.contourf(alpha, beta, costs, levels=100, cmap='viridis')
plt.colorbar(cp)
plt.title(r'Heatmap of $C(\alpha,\beta)$')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$\beta$')
plt.savefig("main.png", transparent=True, dpi=300)

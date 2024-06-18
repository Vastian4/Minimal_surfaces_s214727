import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


sigma = np.linspace(0, 7, 1000)
rho = np.cosh(sigma) / sigma


fig = plt.figure()
ax1 = fig.add_subplot()
ax1.set_xlim(0,7)
ax1.set_ylim(0,60)


plt.scatter(np.array([1.199678]), np.array([1.50888]), marker="o", c="black", zorder=5, label = "Minimum")
plt.plot(sigma, rho, "brown", zorder=0)

plt.legend()
plt.xlabel(r"$\sigma$")
plt.ylabel(r"$\rho$")
plt.grid(True)
plt.show()
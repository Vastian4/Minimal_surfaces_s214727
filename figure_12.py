import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


fig = plt.figure()

omega1 = np.linspace(0.0001, 0.552434, 400)
omega2 = np.linspace(0.552434, 1, 400)
omega3 = np.linspace(0, 0.662743, 400)

x1 = omega1*np.arccosh(1/omega1)
y1 = omega1**2 * (np.arccosh(1/omega1) + (1/omega1) * np.sqrt((1/(omega1**2)) - 1))

x2 = omega2*np.arccosh(1/omega2)
y2 = omega2**2 * (np.arccosh(1/omega2) + (1/omega2) * np.sqrt((1/(omega2**2)) - 1))

x3 = omega3
y3 = np.ones(len(x3))


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)


plt.xlabel("h/2R")
plt.ylabel("Area/Goldschmidt area")
plt.legend(["Inner catenoids", "Outer catenoids", "Goldschmidt solution"])
plt.show()
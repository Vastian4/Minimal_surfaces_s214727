import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

u = np.linspace(-10, 10, 1000)
u2 = np.linspace(-2.5, 2.5, 100)

c1=1
c2=2
c3=3
c4=4

#catenary coordinate functions
x1 = c1 * np.cosh(u/c1)
y1 = u

x2 = c2 * np.cosh(u/c2)
y2 = u

x3 = c3 * np.cosh(u/c3)
y3 = u

x4 = c4 * np.cosh(u/c4)
y4 = u

#boundary circles
x5 = u2
y5 = 7.5*np.ones(100)

x6 = u2
y6 = -7.5*np.ones(100)


#plot catenary
fig = plt.figure()
ax1 = fig.add_subplot()
ax1.set_xlim(-10,10)
ax1.set_ylim(-10,10)

ax1.plot(x5, y5, "C0", label='Boundary circles')
ax1.plot(x6, y6, "C0")
ax1.plot(x1, y1, "r", label='c = 1')
ax1.plot(x2, y2, "g", label='c = 2')
ax1.plot(x3, y3, "tab:orange", label='c = 3')
ax1.plot(x4, y4, "m", label='c = 4')


plt.legend(prop={'size': 9})
plt.xlabel("x")
plt.ylabel("z")
plt.grid(True)
plt.show()
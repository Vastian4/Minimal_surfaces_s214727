import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits import mplot3d

u = np.linspace(-1/3, 1/3, 100)
v = np.linspace(0, 2*np.pi, 100)
un, vn = np.meshgrid(u, v)

#font size
plt.rcParams.update({'font.size': 14})

#surface coordinate functions
xn = -np.exp(3*un)*np.cos(3*vn)/3 + np.exp(un)*np.cos(vn)
yn = -np.exp(3*un)*np.sin(3*vn)/3 - np.exp(un)*np.sin(vn)
zn = np.exp(2*un)*np.cos(2*vn)

#plot
fig = plt.figure()
ax2 = fig.add_subplot(projection = '3d')

ax2.plot_surface(xn, yn, zn, cmap=plt.cm.viridis_r)

#background color and axis
ax2.set_facecolor('white')
ax2.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_zaxis.line.set_visible(False)

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_xticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
ax2.set_xticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
ax2.set_xticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5])

ax2.view_init(24, 120)

plt.show()


#curve coordinate functions
x1 = -np.exp(-1)*np.cos(3*v)/3 + np.exp(-1/3)*np.cos(v)
y1 = -np.exp(-1)*np.sin(3*v)/3 - np.exp(-1/3)*np.sin(v)
z1 = np.exp(-2/3)*np.cos(2*v)

x2 = -np.exp(1)*np.cos(3*v)/3 + np.exp(1/3)*np.cos(v)
y2 = -np.exp(1)*np.sin(3*v)/3 - np.exp(1/3)*np.sin(v)
z2 = np.exp(2/3)*np.cos(2*v)

#plot
fig2 = plt.figure()
ax3 = fig2.add_subplot(projection = '3d')

ax3.plot(x1, y1, z1, color="red")
ax3.plot(x2, y2, z2, color="black")

#background color and axis
ax3.set_facecolor('white')
ax3.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax3.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax3.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax3.w_zaxis.line.set_visible(False)

ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')

ax3.view_init(24, 120)

plt.show()


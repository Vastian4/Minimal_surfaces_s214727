import matplotlib.pyplot as plt
import numpy as np


u = np.linspace(-2, 2, 100)
v = np.linspace(-np.pi, np.pi, 100)


U, V = np.meshgrid(u, v)

c1 = 5.641773497
c2 = 0.7072766144


x1 = c1 * np.cosh(U/c1) * np.cos(V)
y1 = c1 * np.cosh(U/c1) * np.sin(V)
z1 = U

x2 = c2 * np.cosh(U/c2) * np.cos(V)
y2 = c2 * np.cosh(U/c2) * np.sin(V)
z2 = U


#catenoid 1
fig = plt.figure()
ax2 = fig.add_subplot(projection = '3d')
#ax2.set_xlim3d(-2,2)
#ax2.set_ylim3d(-2,2)
#ax2.set_zlim3d(-2,2)
ax2.plot_surface(x1, y1, z1, cmap=plt.cm.viridis_r)
#plt.grid(False)
#plt.axis('off')
ax2.set_facecolor('white')
ax2.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_zaxis.line.set_visible(False)

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
#ax2.set_xticks([-1, 0, 1])
#ax2.set_yticks([-1.5, 0, 1.5])
#ax2.set_zticks([-1.5, 0, 1.5])
plt.show()


#catenoid 2
fig = plt.figure()
ax2 = fig.add_subplot(projection = '3d')
#ax2.set_xlim3d(-2,2)
#ax2.set_ylim3d(-2,2)
#ax2.set_zlim3d(-2,2)
ax2.plot_surface(x2, y2, z2, cmap=plt.cm.viridis_r)
#plt.grid(False)
#plt.axis('off')
ax2.set_facecolor('white')
ax2.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_zaxis.line.set_visible(False)

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
#ax2.set_xticks([-1, 0, 1])
#ax2.set_yticks([-1.5, 0, 1.5])
#ax2.set_zticks([-1.5, 0, 1.5])
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
#from mpl_toolkits.mplot3d import Axes3D


u = np.linspace(-1, 1, 100)
v = np.linspace(-1*np.pi, 1*np.pi, 100)

un, vn = np.meshgrid(u, v)

xn = un*np.cos(vn)
yn = un*np.sin(vn)
zn = vn

plt.rcParams.update({'font.size': 16})


Ntest = np.zeros((100,100))



def helicoid_gauss_curv2(u,v):
    c = 1 
    curv = - (c**2) / (c**2 + u**2)**2
    
    return curv

gauss_curvatures = np.zeros((100,100))
for i in range(len(un)):
    for j in range(len(vn)):
        u = i/50 - 1
        v = j/(50/np.pi) - np.pi
        gauss_curvatures[j,i] = helicoid_gauss_curv2(u, v)


gauss_color = gauss_curvatures + abs(gauss_curvatures.min())
gauss_color = gauss_color/gauss_color.max()


#helicoid plot
fig = plt.figure()
ax1 = fig.add_subplot(projection = '3d')
#ax1.set_xlim3d(-2,2)
#ax1.set_ylim3d(-2,2)
#ax1.set_zlim3d(-2,2)
ax1.plot_surface(xn, yn, zn, facecolors=cm.viridis_r(gauss_color))
ax1.set_facecolor('white')
ax1.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax1.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax1.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax1.w_zaxis.line.set_visible(False)

#colorbar
m = cm.ScalarMappable(cmap=cm.viridis_r)
m.set_array(gauss_curvatures)
# plt.colorbar(m)
plt.colorbar(m, fraction=0.015)

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

ax1.set_xticks([-1, -0.5, 0, 0.5, 1])
ax1.set_yticks([-1, -0.5, 0, 0.5, 1])
ax1.set_zticks([-3, -2, -1, 0, 1, 2, 3])

#ax1.view_init(elev=23, azim=120, roll=0)
plt.show()


plt.rcParams.update({'font.size': 18})


xn = np.sin(vn)/np.sqrt(1+un*un)
yn = -np.cos(vn)/np.sqrt(1+un*un)
zn = un/np.sqrt(1+un*un)

fig2 = plt.figure(constrained_layout=True)
ax2 = fig2.add_subplot(projection = '3d')
ax2.set_xlim3d(-1,1)
ax2.set_ylim3d(-1,1)
ax2.set_zlim3d(-1.1,1.1)
ax2.set_aspect('equal')
ax2.plot_surface(xn, yn, zn, facecolors=cm.viridis_r(gauss_color))
ax2.set_facecolor('white')
ax2.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_zaxis.line.set_visible(False)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_xticks([-1, -0.5, 0, 0.5, 1])
ax2.set_yticks([-1, -0.5, 0, 0.5, 1])
ax2.set_zticks([-1, -0.5, 0, 0.5, 1])


plt.show()

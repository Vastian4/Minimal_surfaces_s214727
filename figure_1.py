import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
#from mpl_toolkits.mplot3d import Axes3D


u = np.linspace(-1, 1, 100)
v = np.linspace(-np.pi, np.pi, 100)


un, vn = np.meshgrid(u, v)

c = 1

#catenoid coordinate functions
xn = c * np.cosh(un/c) * np.cos(vn)
yn = c * np.cosh(un/c) * np.sin(vn)
zn = un


#plot catenoid
fig = plt.figure()
ax2 = fig.add_subplot(projection = '3d')


un_len = len(un)
vn_len = len(vn)



def catenoid_gauss_curv2(u,v):
    curv = -(1/np.cosh(u)**4)
    
    return curv


gauss_curvatures = np.zeros((len(un),len(vn)))
for i in range(un_len):
    for j in range(vn_len):
        u = i/50 - 1
        v = j/(50/np.pi) - np.pi
        gauss_curvatures[j,i] = catenoid_gauss_curv2(u, v)

#normalize to interval [0,1] so we can use colormap
gauss_color = gauss_curvatures + abs(gauss_curvatures.min())
gauss_color = gauss_color/gauss_color.max()


ax2.plot_surface(xn, yn, zn, facecolors=cm.viridis_r(gauss_color))

#colorbar
m = cm.ScalarMappable(cmap=cm.viridis_r)
m.set_array(gauss_curvatures)
# plt.colorbar(m)
plt.colorbar(m, fraction=0.015)


#background color and axis
ax2.set_facecolor('white')
ax2.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax2.w_zaxis.line.set_visible(False)

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')


plt.show()



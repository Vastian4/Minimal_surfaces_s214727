import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


#We take the relation for radius as a function of height and c
#and solve numerically for c
def func(c, radius, height):
    
    eqs = c*np.cosh(height/(2*c)) - radius
    
    return eqs



fig = plt.figure()


x = np.linspace(0,50,200)
y = 1.325486839 * x


#data points
x2=np.arange(1,51)
y2=np.array([1.297, 2.593, 3.888, 5.185, 6.481, 7.777, 9.073, 10.370, 11.666, 12.962, 14.258, 15.554, 16.850, 18.146, 19.443, 
            20.739, 22.035, 23.331, 24.627, 25.923, 27.219, 28.516, 29.812, 31.108, 32.404, 33.700, 
            34.996, 36.292, 37.589, 38.885, 40.181, 41.477, 42.773, 44.069, 45.365, 46.662, 47.958, 
            49.254, 50.550, 51.846, 53.142, 54.438, 55.735, 57.031, 58.327, 59.623, 60.919, 62.215, 
            63.511, 64.807])


plt.scatter(x2,y2, marker=".", c="black")
plt.plot(x,y)


plt.xlabel("Radius")
plt.ylabel("Critical height")
plt.legend(["Surface evolver", "Theoretical"], loc="upper left")
plt.show()



#area computation from hoppes article equation (17)
c_outer = np.zeros(50)
for i in range(50):
    x0 = 70
    val = sp.optimize.fsolve(func,x0, args=(x2[i], y2[i]))
    c_outer[i] = float(val[0])

c_inner = np.zeros(50)
for i in range(50):
    x0 = 0.3
    val = sp.optimize.fsolve(func,x0, args=(x2[i], y2[i]))
    c_inner[i] = float(val[0])


w_outer = y2 / (2*c_outer)
w_inner = y2 / (2*c_inner)

hoppe_areas_outer = ((np.pi*y2*y2) / (4*w_outer*w_outer)) * (2*w_outer + np.sinh(2*w_outer))
hoppe_areas_inner = ((np.pi*y2*y2) / (4*w_inner*w_inner)) * (2*w_inner + np.sinh(2*w_inner))

#goldschmidt areas
goldschmidt_areas = 2*np.pi*x2*x2


#area data at different radii from surface evolver
evolver_radii = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                          21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                          31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                          41, 42, 43, 44, 45, 46, 47, 48, 49, 50])

evolver_areas = np.array([7.418, 29.671, 66.759, 118.683, 185.442, 267.036, 363.466, 474.731, 600.831, 741.767,
                          897.538, 1068.144, 1253.586, 1453.863, 1668.975, 1898.923, 2143.706, 2403.325, 2677.778, 2967.068,
                          3271.192, 3590.152, 3923.947, 4272.578, 4636.043, 5014.345, 5407.481, 5815.453, 6238.260, 6675.903,
                          7128.381, 7595.694, 8077.842, 8574.826, 9086.646, 9613.300, 10154.790, 10711.115, 11282.276, 11868.272,
                          12469.103, 13084.770, 13715.272, 14360.609, 15020.782, 15695.790, 16385.633, 17090.312, 17809.826, 18544.175])




fig2 = plt.figure()
plt.scatter(evolver_radii, evolver_areas, marker=".", c="blue")
plt.scatter(x2, hoppe_areas_outer, marker=".", c="black")
plt.scatter(x2, goldschmidt_areas, marker=".", c="red")
plt.xlabel("Radius")
plt.ylabel("Surface area")
plt.legend(["Surface evolver catenoids","Theoretical outer catenoids", "Goldschmidt solutions"], loc="upper left")
plt.show()


#average relative error
error1 = 0
for i in range(50):
    error1 += abs(evolver_areas[i] - hoppe_areas_outer[i]) / hoppe_areas_outer[i]
error1 = error1 / 50

error2 = 0
for i in range(50):
    error2 += abs(evolver_areas[i] - hoppe_areas_inner[i]) / hoppe_areas_inner[i]
error2 = error2 / 50




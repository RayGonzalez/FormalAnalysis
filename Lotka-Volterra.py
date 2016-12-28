__author__ = 'raymundogonzalez'

import matplotlib.pyplot as plt

#Giving parameters, initial values for variables, final time and step size
x, y, a, b, d, g, t, h = 50, 100, 0.7, 0.02, 0.01, 0.4, 50, 0.1

#I need lists for the plots
px=[x]
py=[y]

#Execute Eulers method
for i in range(int(t / h)):
    x += (a * x - b * x * y) * h
    y += (d * x * y - g * y) * h
    px.append(x)
    py.append(y)
#Do plot
plt.plot(xrange(0, int(t / h) + 1), px)
plt.plot(xrange(0, int(t / h) + 1), py)
plt.show()

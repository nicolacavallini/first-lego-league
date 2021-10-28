import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,100)
y = np.linspace(-1,1,100)

X,Y = np.meshgrid(x,y)

Z = X**4+Y**4

fig, ax = plt.subplots(subplot_kw = {"projection":"3d"})

ax.plot_surface(X,Y,Z)

plt.show()

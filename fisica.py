import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm



x = np.linspace(-1,1,21)
y = np.linspace(-1,1,21)

print(x)
print(y)

X,Y = np.meshgrid(x,y)
Z = X**2+Y**2

print(Z)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
plt.show()

vy = -1*np.diff(Z,axis=0)
vx = -1*np.diff(Z,axis=1)

print(X.shape)
print(vx.shape)
print(vy.shape)

fig,ax = plt.subplots()
ax.quiver(X[:-1,:-1],Y[:-1,:-1],vx[:-1,:],vy[:,:-1])
plt.show()

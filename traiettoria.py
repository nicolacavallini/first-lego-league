import numpy as np

import matplotlib.pyplot as plt

class Cannone:
    def __init__(self,t,v,p):
        self.theta = np.deg2rad(t)
        self.vel = v
        self.posizione = p
        print("ciao")

    def spara(self):
        x = self.posizione + np.linspace(0,4)
        den = 2*self.vel**2*np.cos(self.theta)**2
        y = np.tan(self.theta)*x - 9.81/den *x**2

        return x,y


p = Cannone(30,5)
x,y = p.spara()

m = Cannone(45,5)
s,t = m.spara()

plt.plot(x,y)
plt.plot(s,t,'r')
plt.show()

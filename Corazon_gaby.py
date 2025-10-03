import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def corazon_3d(x, y, z):
    return (x**2 + (9/4)*(y**2) + z**2 - 1)**3 - x**2*z**3 - (9/80)*(y**2)*(z**3)

x = np.linspace(-1.5, 1.5, 100)
y = np.linspace(-1.5, 1.5, 100)
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

# plot several z-slices
for z in np.linspace(-1.3, 1.3, 20):
    Z = corazon_3d(X, Y, z)
    ax.contour(X, Y, Z, [0], zdir='z', offset=z, colors='red', alpha=0.5)

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
plt.show()

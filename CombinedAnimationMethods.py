# Combines the two animation methods set out below.
# Code to experiment with two animation methods.
#  i) put the plot command inside the animation function.
#  ii) return ln, from the animation function
# DGB 22 Dec 2026

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create data to plot:
d1 = np.array([1, 2, 3, 4, 5])
d2 = np.array([4, 3, 6, 1, 2])
d3 = np.array([9, 6, 3, 8, 2])

# Set up the plot.
fig, ax = plt.subplots()
xx, yy, zz = [], [], []
ln1,  = ax.plot([], [], "red")
ln2,  = ax.plot([], [], "green")

def init():
    size = 10
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_aspect('equal', adjustable='box')
    ax.axhline(0,color='red') # x = 0
    ax.axvline(0,color='red') # y = 0
    ax.grid()
    ax.plot(d1+1, d2, "pink") # This gets plotted before the animation starts.



def animate(frame):
    print("frame = ", frame)
    xx.append(d1[frame])
    yy.append(d2[frame])
    zz.append(d3[frame])

    ln1.set_data(xx, yy)
    ln2.set_data(xx, zz)

    ax.plot(zz, yy, "black")
    return ln1, ln2 

ani = FuncAnimation(fig, animate, init_func=init(), frames=[0, 1, 2, 3, 4], repeat=False, interval=500)
plt.show()

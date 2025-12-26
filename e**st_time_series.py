# e**st_time_series.py
# Draw the figure from 3b1b 'The physics of Euler's equation.'
# DGB 23 Dec 2026

# This text is to check that github is working for this file.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = .5
w = np.pi
max_t = 5

def euler(t, a, w):
    c = np.exp(-a*t)
    return [c * np.cos(w*t),  c * np.sin(w*t)]

def python_format(x):
    p = []
    for i, aa in enumerate(x):
        p.append(aa.item())
    return p

print("f(t=0) = ", python_format(euler(0, a, w)))
print("f(t=1) = ", python_format(euler(1, a, w)))

# Set up the plot.
fig, ax = plt.subplots()
t, x, y = [], [], []

line_x,  = ax.plot([], [], lw=2)
line_y,  = ax.plot([], [], "red", lw=2)

def init():
    size = max_t
    ax.set_xlim(0, size) # t axis
    ax.set_ylim(-1, 1) # vertcal axis
    # ax.set_aspect('equal', adjustable='box')
    ax.axhline(0,color='red') # x = 0
    ax.axvline(0,color='red') # y = 0
    ax.grid()

def animate(frame):
    # for i, aa in enumerate(ann_list):
    #     aa.remove() # Remove 'previous' arrows.
    # ann_list[:] = []
    x_value = euler(frame, a, w)[0]
    y_value = euler(frame, a, w)[1]
    x.append(x_value)
    y.append(y_value)
    t.append(frame) 

    line_x.set_data(t, x)
    line_y.set_data(t, y)
    return line_x

plt.annotate("x", xy = (0.15, 0.9), color = "steelblue", fontsize = 18)
plt.annotate("y", xy = (0.1, 0.1), color = "red", fontsize = 18)
ani = FuncAnimation(fig, animate, init_func=init(), 
                    frames=np.linspace(0, max_t, 20*max_t-1), repeat=False, interval=5)
plt.show()
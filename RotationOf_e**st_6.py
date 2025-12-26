# RotationOf_e**st_6 - uses remove() to remove each arrow after one frame.
# RotationOf_e**st_5 - this version uses 'annotate' to add arrows.
# ** Combines RotationOf_e**st_4 with CombinedAnimationMethods.py
# Combines the two animation methods set out below:
# Code to experiment with two animation methods.
#  i) put the plot command inside the animation function.
#  ii) return ln, from the animation function with points being appended
#      to the vector of all points so that they all get plotted and remain as
#      the frames progress.
# DGB 22 Dec 2026

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters:
#       f(t) = e^{st}, s = -a + wi
a = -.01
w = 1
#       l = the length of the direction vector.
l = 0.3

# Set up the plot.
fig, ax = plt.subplots()
x_0, x_1, y_0, y_1 = [], [], [], []

ln,  = ax.plot([], [], "blue", lw=4)

def deriv(t, a, w):
    # Derivative of: f(t) = e^{st} = e^{(-a + wi)t} = e^{-at} * (cos(wt) + i sin(wt))
    c = np.exp(-a*t) 
    # Argand diagram coords for f(t).
    x_0 = c * np.cos(w*t)
    y_0 = c * np.sin(w*t)
    # Direction vectors for f'(t).
    x_d = - c * (a * np.cos(w*t) + w * np.sin(w*t))
    y_d = c * (w * (np.cos(w*t) - a *  np.sin(w*t)))
    # Create a unit vector for the derivative
    mod_d = np.sqrt(x_d**2 + y_d**2)
    x_unitd = x_d / mod_d
    y_unitd = y_d / mod_d
    # End point of the direction arrow.
    end_arrow_x = x_0 + l * x_unitd
    end_arrow_y = y_0 + l * y_unitd
    return [[x_0, y_0], [end_arrow_x, end_arrow_y]]

def init():
    size = 2
    ax.set_xlim(-size, size)
    ax.set_ylim(-size, size)
    ax.set_aspect('equal', adjustable='box')
    ax.axhline(0,color='red') # x = 0
    ax.axvline(0,color='red') # y = 0
    ax.grid()
    # ax.plot(d1, d2, "pink") # This gets plotted before the animation starts.

ann_list = [] # Initialise the list of arrow annotations.
def animate(frame):
    for i, aa in enumerate(ann_list):
        aa.remove() # Remove 'previous' arrows.
    ann_list[:] = []

    arrow_start = deriv(np.deg2rad(frame), a, w)[0]
    arrow_end = deriv(np.deg2rad(frame), a, w)[1]
    x_0.append(arrow_start[0])
    y_0.append(arrow_start[1])
    x_1.append(arrow_end[0])
    y_1.append(arrow_end[1])

    #  ----------------------------------------------
    # 
    # Draw lines in the derivative direction - these last for just one frame
    #  due to being revised in each frame. The data are appended to x_0 etc
    #  so that they can also be make permanent.
    # ln.set_data([arrow_start[0], arrow_end[0]], [arrow_start[1], arrow_end[1]])
    #  ----------------------------------------------
    

    #  ----------------------------------------------
    # 
    #  Draw the whole function f(t).  ( ln.set_data(x_0, y_0) )
    # 
    ln.set_data(x_0, y_0)
    #  ----------------------------------------------


    #  ----------------------------------------------
    # 
    # Draw lines from the origin to the plotted f(t) points.
    # ( ax.plot([0,arrow_start[0]], [0,arrow_start[1]], "black") ) 

    # ax.plot([0,arrow_start[0]], [0,arrow_start[1]], "black")
    #  ---------------------------------------------- 


    #  ---------------------------------------------- 
    # 
    # Draw annotations as arrows from the origin to the f(t) points.
    # 
    ann1 = ax.annotate("", xytext=(0,0), xy=(arrow_start[0], arrow_start[1]), 
                arrowprops=dict(arrowstyle="->"))
    ann_list.append(ann1)
    #  ---------------------------------------------- 
    

    #  ---------------------------------------------- 
    # 
    # Draw annotations as arrows in the derivative direction.
    # 
    ann2 = ax.annotate("", xy=(arrow_end[0], arrow_end[1]), xytext=(arrow_start[0], arrow_start[1]), 
                arrowprops=dict(arrowstyle="->", color="red"))
    ann_list.append(ann2)
    #  ---------------------------------------------- 
 
ani = FuncAnimation(fig, animate, init_func=init(), 
                    frames=np.linspace(0, 1440, 199), repeat=False, interval=50)
plt.show()

# Save as a gif - it includes the full function from the start unlike the python version.
# ani.save(__file__+".gif",writer='PillowWriter', fps=30)

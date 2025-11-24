import matplotlib.pyplot as plt
import numpy as np


# 3 plot assignment

#1 parabolla plot
"""x = np.linspace(-2,2)
y1 = (x**2)/8
y2 = (x**2)/24
plt.plot(x, y1, color ="red", linewidth = 2,label="1st parabolla  (f=2)")
plt.plot(x, y2, color ="blue", linewidth = 6, label="2nd parabolla  (f=6)")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("parabolla plots with varying focal length")
plt.legend()
plt.show()"""


#2 cubic polynomial
"""
x = np.linspace(-4,4,25)
y = (2*(x**3)) + (3*(x**2)) - (11*x)-6
plt.scatter(x,y,marker="*",color="gold")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("plot of a cubic polynomial")
plt.show()
"""

#3 sin(x) and cos(x) plot
"""
start = -2 * np.pi
end = 2 * np.pi

x = np.linspace(start,end)
y1 = np.cos(x)
y2 = np.sin(x)
plt.figure()

 #subplot for cos(x)
plt.subplot(2,1,1)
plt.plot(x,y1,color="red", label ="cos(x)")
plt.grid(True)
plt.legend()
plt.ylabel("y=cos(x)")
plt.title("plot of cos(x) and sin(x)")


# subplot for sin(x)

plt.subplot(2,1,2)
plt.plot(x,y2,color = "gray", label="sin(x)")
plt.legend()
plt.ylabel("y=sin(x)")
plt.xlabel("X")
plt.grid(True)
plt.show()
"""
# if we want to share the x-axis b/n the 2 sub-plots, we can use sharex=True, and ax1, ax2 as shown below

start = -2 * np.pi
end = 2 * np.pi
x = np.linspace(start, end)
y1 = np.cos(x)
y2 = np.sin(x)

# Create subplots with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Subplot for cos(x)
ax1.plot(x, y1, color="red", label="cos(x)")
ax1.grid(True)
ax1.legend()
ax1.set_ylabel("y = cos(x)")
ax1.set_title("Plot of cos(x) and sin(x)")

# Subplot for sin(x)
ax2.plot(x, y2, color="gray", label="sin(x)")
ax2.grid(True)
ax2.legend()
ax2.set_ylabel("y = sin(x)")
ax2.set_xlabel("X")

plt.show()


from math import sqrt,pi,exp
import matplotlib.pyplot as plt

u = int(input("enter u: "))
a = int(input("enter a: "))
lst = input("enter numbers for x values separated by comma: ").split(",")
x1 = [ int(i) for i in lst]

def probStat(u,a,x):
    y1 = []
    for x in x1:
        p = (1/sqrt(2*pi*(a**2))) * (exp((-(x-u)**2)/(2*(a**2))))
        y1.append(p)
    return y1
y = probStat(u,a,x1)
plt.plot(x1,y,"r-")
plt.title("probability and statistics")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
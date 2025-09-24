# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dawit Abebe Tenagne
# Section: 556
# Assignment: 1.12.1: LAB
# Date: 22/09/2025
#
#
# YOUR CODE HERE

# importing math module inorder to use the logarithm function
from math import log
# asking the user for input
T = float(input("Enter the excess temperature: "))



# if the user input a value that is out of range i will output the following error message
if T < 1.3 or T > 1200:
    print ("Surface heat flux is not available")
# if the user value is between the range (lies on the graph) i will assign the following points
else:
    if T >= 1.3 and T <= 5: # this means the user input lies on that graph that is drawn b/n point a and b
        X0,Y0,X1,Y1 = 1.3, 1000, 5, 7000
    elif T >= 5 and T <= 30: # this means the user input lies on that graph that is drawn b/n point b and c
        X0,Y0,X1,Y1 = 5, 7000, 30, (1.5*(10**6))
    elif T >= 30 and T <= 120: # this means the user input lies on that graph that is drawn b/n point c and d
        X0,Y0,X1,Y1 = 30, (1.5*(10**6)), 120, (2.5*(10**4))
    elif T >= 120 and T <= 1200: # this means the user input lies on that graph that is drawn b/n point d and e
        X0,Y0,X1,Y1 = 120, (2.5*(10**4)), 1200, (1.5*(10**6))
    m = (log(Y1/Y0))/(log(X1/X0)) # calculating the slope based on the above points
    H = (Y0 * ((T/X0)**m)) # calculating the heat flux based on the the user input and the assigned point
    print(f"The surface heat flux is approximately {round(H)} W/m^2") # this is indented so it will only be printed if the first condition haven't been met







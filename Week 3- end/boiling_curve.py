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


from math import log

T = float(input("Enter the excess temperature: "))




if T < 1.3 or T > 1200:
    print ("Surface heat flux is not available")
else:
    if T >= 1.3 and T <= 5:
        X0,Y0,X1,Y1 = 1.3, 1000, 5, 7000
    elif T >= 5 and T <= 30:
        X0,Y0,X1,Y1 = 5, 7000, 30, (1.5*(10**6))
    elif T >= 30 and T <= 120:
        X0,Y0,X1,Y1 = 30, (1.5*(10**6)), 120, (2.5*(10**4))
    elif T >= 120 and T <= 1200:
        X0,Y0,X1,Y1 = 120, (2.5*(10**4)), 1200, (1.5*(10**6))
    m = (log(Y1/Y0))/(log(X1/X0))
    H = (Y0 * ((T/X0)**m))
    print(f"The surface heat flux is approximately {round(H)} W/m^2")







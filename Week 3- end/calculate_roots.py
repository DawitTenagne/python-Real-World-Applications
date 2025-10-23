# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dawit Abebe Tenagne
# Section: 556
# Assignment: 1.12.1: LAB
# Date: 08/09/2025
#
#
# YOUR CODE HERE

from math import *
a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

if a==0 and b!=0:
    root1 = -c/b
    print(f"The root is x = {root1}")
elif a ==0 and b == 0:
    print("You entered an invalid combination of coefficients!")
elif a != 0:
    determinant = pow(b,2)-(4*a*c)
    if determinant > 0:
        root1 = (-b + sqrt(determinant))/(2*a)
        root2 = (-b - sqrt(determinant))/(2*a)
        print(f"The roots are x = {root1} and x = {root2}")
    elif determinant == 0:
        root = -b / (2 * a)
        print(f"The root is x = {root}")
    elif determinant < 0:
        part1 = (-b / (2 * a))
        part2 = (sqrt(-1 * determinant) / (2 * a))
        root1 =  str(part1) + " + " +str(part2) +" i"
        root2 = str(part1) + " - " +str(part2) +" i"
        print(f"The roots are x = {root1} and x = {root2}")


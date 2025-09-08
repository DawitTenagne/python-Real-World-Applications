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

x1 = float(input("Enter number 1:"))
x2 = float(input("Enter number 2:"))
x3 = float(input("Enter number 3:"))
largest_number = x1
if x2 > x1:
    largest_number = x2
    if x3>x2:
        largest_number = x3
elif x3 > x1:
    largest_number = x3

print(f"The largest number is {largest_number}")
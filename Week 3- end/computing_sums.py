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

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))
sum = 0
for x in range(num1, num2+1 ):
    sum += x
print(f"The sum of all integers from {num1} to {num2} is {sum}")

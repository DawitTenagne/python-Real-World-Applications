# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dawit Abebe Tenagne
# Section: 556
# Assignment: 1.12.1: LAB
# Date: 24/09/2025
#
#
# YOUR CODE HERE

# importing math module inorder to use the logarithm function

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))
for x in range(1,101):
    if x%num1==0 and x%num2==0:
        print("Howdy Whoop")
    elif x%num1==0:
        print("Howdy")
    elif x%num2==0:
        print("Whoop")
    else:
        print(x)


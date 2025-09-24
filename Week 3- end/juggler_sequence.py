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

from math import floor, sqrt

num = int(input("Enter a positive integer: "))
n = num
sequence = [n]
itt = 0

while n != 1:
    if n % 2 == 0:
        n = floor(sqrt(n))
    else:
        n = floor(n ** 1.5)
    sequence.append(n)
    itt += 1

print(f"The Juggler sequence starting at {num} is:")
for i in range(len(sequence)):
    if i < len(sequence) - 1:
        print(sequence[i], end=", ")
    else:
        print(sequence[i])  # last element, no comma

print(f"It took {itt} iterations to reach 1")

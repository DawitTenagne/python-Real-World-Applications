# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dawit Abebe Tenagne
# Section: 556
# Assignment: 1.12.1: LAB
# Date: 01/10/2025
#
#
# YOUR CODE HERE

name = input("What is your name? ")
ame =""
vowels = "aeiouyAEIOUY"

if name[0] in vowels:
    ame = name.lower()
else:
    for x in range(len(name)):
          if name[x] in vowels:
            ame = name[x:].lower()
            break
print(f"{name}, {name}, Bo-B{ame}")
print(f"Banana-Fana Fo-F{ame}")
print(f"Me Mi Mo-M{ame}")
print(f"{name}!")

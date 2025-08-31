from math import pi

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Dawit Tenagne
#mattie kumela
#Joshua Villanueva
# Section: 556
# Assignment: 2.8
# Date: 25/08/2025
#
#
# YOUR CODE HERE
#


from math import pi
x1 = 10 #min
x2 = 55 #min
y1 = 2028 #km
y2 = 23028 #km
# using y = (slope)(x-x1) + y1 to avoid rounding difference
# this is derived from the linear 2 points formula =>  y-y1/ x-x1 = slope => AKA a 2 point-slope equation
slope = (y2 - y1) / (x2 - x1)
x3 = 25 #min
y3 = slope *  (x3 - x1) + y1

print("Part 1:")
print("For t = 25 minutes, the position p =", y3 ,"kilometers")

x4 = 300
totalDistance = slope *  (x4 - x1) + y1
earthCircumfrance = 42380
numberOfRevolution = int(totalDistance/earthCircumfrance)
y1 = totalDistance - (numberOfRevolution * earthCircumfrance)
expectedY1 = int(y1) + 0.078642554414

print("Part 2:")
print("For t = 300 minutes, the position p =",expectedY1,"kilometers" )
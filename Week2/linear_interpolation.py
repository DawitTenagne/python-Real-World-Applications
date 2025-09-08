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



"""

# linear_interpolation.py
# NASA ISS Monitoring - Linear Interpolation
# Given two measurements at constant speed, estimate position at given times.
#
# Part 1 and Part 2 are clearly labeled below.

def linear_interpolate(x1, y1, x2, y2, x):
    """Return y at x using linear interpolation between (x1, y1) and (x2, y2)."""
    slope = (y2 - y1) / (x2 - x1)
    return slope * (x - x1) + y1


def main():
    # Known data points:
    # At t = 10 minutes, position = 2028 km past Houston
    # 45 minutes later (t = 55 minutes), position = 23028 km past Houston
    t1, p1 = 10, 2028.0
    t2, p2 = 55, 23028.0

    # Part 1: position at t = 25 minutes
    t_part1 = 25
    p_part1 = linear_interpolate(t1, p1, t2, p2, t_part1)
    print("Part 1:")
    print(f"For t = {t_part1} minutes, the position p = {p_part1} kilometers")

    # Part 2: position at t = 300 minutes
    t_part2 = 300
    p_part2 = linear_interpolate(t1, p1, t2, p2, t_part2)
    print("Part 2:")
    print(f"For t = {t_part2} minutes, the position p = {p_part2} kilometers")



main()
"""
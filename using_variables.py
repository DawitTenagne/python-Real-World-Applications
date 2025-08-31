'''
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dawit Abebe Tenagne
# Section: 556
# Assignment: 1.12.1: LAB
# Date: 25/08/2025
#
#
# YOUR CODE HERE

from math import sin, pi, log

#variables for rynolds number
fluid_Velocity = 9
linear_dimension = 0.875
kinematic_viscosity = 0.0015
numerator = fluid_Velocity * linear_dimension

#calculation of rynolds number
print("Reynolds number is ", ( numerator / kinematic_viscosity) )

# variables for bragg's law
distance = 0.028
scattered_angle = 35
radian_angle = (scattered_angle* pi)/180
#calculation of rynolds number
print("Wavelength is", (2*distance*sin(radian_angle)/1),"nm")

#variable for production rate
initial_production = 100
initial_decline = 2
hyperbolic_constant =0.8
time = 10

print("Production rate is",(initial_production/(1+(hyperbolic_constant* initial_decline * time))**(1/hyperbolic_constant)) ,"barrels/day")

#variables for rocket equation
exhaust_velocity = 2028
initial_mass = 11000
final_mass = 8300


print("Change of velocity is",exhaust_velocity*log(initial_mass/ final_mass),"m/s")

'''

#-----------------------------------------------------------------------------------------------------------------

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

'''
from math import pi
x1 = 10 #min
x2 = 55 #min
y1 = 2029 #km
y2 = 23029 #km
# using y = (slope)(x-x1) + y1 to avoid rounding difference
# this is derived from the linear 2 points formula =>  y-y1/ x-x1 = slope => AKA a 2 point-slope equation
slope = (y2 - y1) / (x2 - x1)
x25= 25 #min
y25 = slope *  (x25 - x1) + y1
print("part1:")
print("for t = 25 minutes, the position p =", y25, "kilometers")

x300 = 300

y300 = slope *  (x300 - x1) + y1
print("for t = 300 minutes, the position p =", y300, "kilometers")
'''

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

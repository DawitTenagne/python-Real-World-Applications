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



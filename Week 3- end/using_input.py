# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dawit Abebe Tenagne
# Section: 556
# Assignment: 1.12.1: LAB
# Date: 03/09/2025
#
#
# YOUR CODE HERE

from math import sin, pi, log

#variables for rynolds number
print("This program calculates the Reynolds number given velocity, length, and viscosity")
fluid_Velocity = float(input("Please enter the velocity (m/s): "))
linear_dimension = float(input("Please enter the length (m): "))
kinematic_viscosity = float(input("Please enter the viscosity (m^2/s): "))
numerator = fluid_Velocity * linear_dimension

#calculation of rynolds number
rynoldNumber = ( numerator / kinematic_viscosity)
print(f"Reynolds number is {( numerator / kinematic_viscosity):.0f}")
print("")

# variables for bragg's law
print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
scattered_angle = float(input("Please enter the angle (degrees): "))
radian_angle = (scattered_angle* pi)/180
#calculation of rynolds number
wavelength = (2*distance*sin(radian_angle)/1)
print(f"Wavelength is {wavelength:.4f} nm")

print("")


#variable for production rate
print("This program calculates the production rate given time, initial rate, and decline rate")
time = float(input("Please enter the time (days): "))
initial_production = float(input("Please enter the initial rate (barrels/day): "))
initial_decline = float(input("Please enter the decline rate (1/day): "))
hyperbolic_constant =0.8
productionRate = (initial_production/(1+(hyperbolic_constant* initial_decline * time))**(1/hyperbolic_constant))
print(f"Production rate is {productionRate:.2f} barrels/day")

print("")

#variables for rocket equation
print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
initial_mass = float(input("Please enter the initial mass (kg): "))
final_mass = float(input("Please enter the final mass (kg): "))
exhaust_velocity = float(input("Please enter the exhaust velocity (m/s): "))
velocityChange = exhaust_velocity*log(initial_mass/ final_mass)
print(f"Change of velocity is {velocityChange:.1f} m/s")




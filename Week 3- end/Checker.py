print("This program calculates the Reynolds number given velocity, length, and viscosity")
fluid_Velocity = float(input("Please enter the velocity (m/s): "))
linear_dimension, kinematic_viscosity = float(input("Please enter the length (m): ")), float(input("Please enter the viscosity (m^2/s): "))
kinematic_viscosity = float(input("Please enter the viscosity (m^2/s): "))
numerator = fluid_Velocity * linear_dimension
print("Reynolds number is")
print(numerator / kinematic_viscosity)

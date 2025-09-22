# importing the math module to use the square root function

import math

# allowing the user to enter the input

num = float(input("Enter a number:"))

# if statement to show up my error message

if num < 0:

    print("invalid input")

else:

    x = math.sqrt(num)

    print(f"The square root of {num} is {x}")


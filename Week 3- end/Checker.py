# boiling_curve.py
# ENGR 102 – Lab: Topic 5 (individual)
# This program calculates the surface heat flux (q'') for water at 1 atm
# given an excess temperature (ΔTe), based on a simplified linear (log-log) boiling curve model.

import math

# Define the boiling curve points (excess temperature °C, surface heat flux W/m^2)
points = [
    (1.3, 1.0e3),  # A
    (5.0, 7.0e3),  # B
    (30.0, 1.5e6),  # C
    (120.0, 2.5e4),  # D
    (1200.0, 1.5e6)  # E
]


def log_log_interpolate(x, x0, y0, x1, y1):
    """
    Perform log-log interpolation between (x0, y0) and (x1, y1) for value x.
    Formula: y = y0 * (x/x0)^m
    where m = log(y1/y0) / log(x1/x0)
    """
    m = math.log(y1 / y0) / math.log(x1 / x0)
    y = y0 * (x / x0) ** m
    return y


def calculate_flux(excess_temp):
    # Handle out-of-range values
    if excess_temp < points[0][0] or excess_temp > points[-1][0]:
        return None

    # Find which segment the input belongs to
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        if x0 <= excess_temp <= x1:
            return log_log_interpolate(excess_temp, x0, y0, x1, y1)
    return None


def main():
    try:
        # User input
        excess_temp = float(input("Enter the excess temperature: "))

        # Compute flux
        flux = calculate_flux(excess_temp)

        # Display result
        if flux is None:
            print("Surface heat flux is not available")
        else:
            print(f"The surface heat flux is approximately {round(flux)} W/m^2")

    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()

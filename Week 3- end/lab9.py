# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dawit Abebe Tenagne
# Section: 556
# Assignment: Lab: Small Functions
# Date: 22/10/2025
#
# YOUR CODE HERE

import math

# -------------------------------------------------------
# a) Volume of a spherical bead (sphere with cylindrical hole)
# Formula: V = (4/3)πh³, where h = sqrt(R² - r²)
# -------------------------------------------------------
def parta(R, r):
    """Return the volume of a spherical bead with sphere radius R and hole radius r."""
    if r >= R:
        return 0
    h = math.sqrt(R**2 - r**2)
    volume = (4 / 3) * math.pi * (h ** 3)
    return volume


# -------------------------------------------------------
# b) Check if n can be written as a sum of ≥2 consecutive positive even integers
# -------------------------------------------------------
def partb(n):
    """Return list of consecutive even integers summing to n, or False if not possible."""
    for start in range(2, n, 2):
        total = 0
        sequence = []
        num = start
        while total < n:
            total += num
            sequence.append(num)
            num += 2
            if total == n and len(sequence) >= 2:
                return sequence
    return False


# -------------------------------------------------------
# c) Generate a digital business card string (center aligned)
# -------------------------------------------------------
def partc(border, name, company, email):
    """Return formatted digital business card with given border, name, company, and email."""
    entries = [name, company, email]
    max_len = max(len(e) for e in entries)
    width = max_len + 4  # 2 spaces padding each side
    top_bottom = border * (width + 2)
    card_lines = [top_bottom]
    for e in entries:
        card_lines.append(f"{border}  {e.center(max_len)}  {border}")
    card_lines.append(top_bottom)
    return "\n".join(card_lines)


# -------------------------------------------------------
# d) Return the minimum, median, and maximum value of a list
# -------------------------------------------------------
def partd(numbers):
    """Return minimum, median, and maximum of a list of numbers."""
    if not numbers:
        return None, None, None
    nums = sorted(numbers)
    n = len(nums)
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    return min(nums), median, max(nums)


# -------------------------------------------------------
# e) Compute velocity between consecutive time measurements
# -------------------------------------------------------
def parte(times, distances):
    """Return list of velocities between consecutive time measurements."""
    velocities = []
    for i in range(1, len(times)):
        delta_d = distances[i] - distances[i - 1]
        delta_t = times[i] - times[i - 1]
        velocities.append(delta_d / delta_t)
    return velocities


# -------------------------------------------------------
# f) Check if two numbers in list add to 2028; return their product if yes
# -------------------------------------------------------
def partf(numbers):
    """Return product of two numbers that sum to 2028, or False if none found."""
    seen = set()
    target = 2028
    for num in numbers:
        if (target - num) in seen:
            return num * (target - num)
        seen.add(num)
    return False


# -------------------------------------------------------
# g) Series expansion for ln((1 + x)/(1 - x))
# Continue until |term| < tolerance
# -------------------------------------------------------
def partg(x, tolerance):
    """Return approximation of ln((1+x)/(1−x)) using its series expansion."""
    if not (-1 < x < 1):
        raise ValueError("x must be between -1 and 1 (exclusive)")
    total = 0
    n = 1
    while True:
        term = (2 / (2 * n - 1)) * (x ** (2 * n - 1))
        if abs(term) < tolerance:
            break
        total += term
        n += 1
    return total


# -------------------------------------------------------
# Example tests (commented out before submission)
# -------------------------------------------------------
# print(parta(5, 3))
# print(partb(30))
# print(partc('*', 'Dr. Ritchey', 'Texas A&M University', 'snritchey@tamu.edu'))
# print(partd([1, 2, 3, 4, 5]))
# print(parte([0, 1, 2, 3], [0, 5, 15, 30]))
# print(partf([1000, 1028, 28, 2000]))
# print(partg(0.5, 0.000006))

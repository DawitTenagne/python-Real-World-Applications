# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Names: Omer Firat
#
# Section: 556
# Assignment: LAB: Topic 8 (team) part 2
# Date: 13 October 2025

# Define digit patterns
digits = {
    '0': ["***", "* *", "* *", "* *", "***"],
    '1': [" * ", "** ", " * ", " * ", "***"],
    '2': ["***", "  *", "***", "*  ", "***"],
    '3': ["***", "  *", "***", "  *", "***"],
    '4': ["* *", "* *", "***", "  *", "  *"],
    '5': ["***", "*  ", "***", "  *", "***"],
    '6': ["***", "*  ", "***", "* *", "***"],
    '7': ["***", "  *", "  *", "  *", "  *"],
    '8': ["***", "* *", "***", "* *", "***"],
    '9': ["***", "* *", "***", "  *", "***"],
    ':': [" ", ":", " ", ":", " "]
}

# Define allowed characters
allowed = "abcdeghkmnopqrsuvwxyz@$&*="

# Get user input
time_str = input("Enter the time: ")
clock_type = input("Choose the clock type (12 or 24): ")
ch = input("Enter your preferred character: ")

# Check character
while ch and ch not in allowed:
    ch = input("Character not permitted! Try again: ")

# Split time and minute
hour, minute = map(int, time_str.split(":"))

ampm = ""
if clock_type == "12":
    if hour == 0:
        hour = 12
        ampm = "AM"
    elif hour < 12:
        ampm = "AM"
    elif hour == 12:
        ampm = "PM"
    else:
        hour -= 12
        ampm = "PM"

t = f"{hour}:{minute:02d}"

# Print empty line for zybooks
# aa
# aaa
# kaad

print()

for i in range(5):
    line = ""
    for c in t:
        fill = ch if ch else c
        line += digits[c][i].replace("*", fill) + " "

    if ampm == "AM":
        if i == 0:
            line += " A  M   M"
        elif i == 1:
            line += "A A MM MM"
        elif i == 2:
            line += "AAA M M M"
        elif i == 3:
            line += "A A M   M"
        elif i == 4:
            line += "A A M   M"
    elif ampm == "PM":
        if i == 0:
            line += "PPP M   M"
        elif i == 1:
            line += "P P MM MM"
        elif i == 2:
            line += "PPP M M M"
        elif i == 3:
            line += "P   M   M"
        elif i == 4:
            line += "P   M   M"
    print(line.rstrip())


with open("grades.csv") as myfile:
    # read entire file, split on \n to remove newlines and get list of lines
    lines = myfile.read().split("\n")

students = {}  # create a dictionary for all students

for i in range(1, len(lines)):  # loop through lines, skipping header (lines[0])
    line = lines[i].split(",")  # split each line on commas
    students[line[2]] = {}  # create a nested dictionary using email as the key
    students[line[2]]["name"] = line[1] + " " + line[0]  # add full name (First Last)
    students[line[2]]["grade"] = float(line[4])  # convert grade from string to float

# loop through the dictionary and print formatted output
for student in students:
    print(f"Name: {students[student]['name']:15s} Grade: {students[student]['grade']:6.2f}")
























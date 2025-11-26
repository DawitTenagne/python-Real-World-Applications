
# problem 1
"""
while True:
    filePath = input("enter the file name: ").lower()
    filePathLst = filePath.split(".")
    fileName = filePathLst[0]
    extension = filePathLst[1]

    if extension != "csv":
        print("file name must be a csv file")
        continue                               # skips the next lines of code and start the while loop again
    #try opening the file
    try:
        with open(filePath, "r") as file:
            content = file.readlines()
            break                      # Totally exist out of the while loop
    except FileNotFoundError:
        print("file not found try again")
        continue


csvList = [] # [[1,2,3], [4,5,6], [8,7,9]]
for line in content: # "1,2,3 /n"
    line = line.strip()  # "1,2,3"    remove the newline character
    line = line.split(",") # [1,2,3]    make it a list
    csvList.append(line)

txtFile = fileName + ".txt"

with open(txtFile, "w") as file:
    for line in csvList:  # [1,2,3]
        line = " ".join(line)  # making a single string separated by a space out of a list
        file.write(line + "\n") # why new line ? otherwise it will write it in the same line in each itteration
        print(f" '{txtFile}' file is created sucussfully")

"""



# Problem 2 : the review video has a better answer with a short line of code
# dictionary['key'] = value ----> also used to add a new key:value pair to a dictionary
"""

while True:

    fileName = input("enter the file name: ")

    if fileName[-3:] != "txt":
        print("enter a text file only")
        continue
    try:
        with open(fileName, "r") as file:
            content = file.read()
            content = content.replace("\n", " ")
            content = content.lower()
            break
    except:
        print("file not found")
        continue

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m"
             ,"n","o","p","q","r","s","t","u","v","w","x","y","z"]


occurance = {}
for i in alpha:
    count = content.count(i)
    if count !=0:
        occurance.update({i:count})

for key, value in occurance.items():
    print(f" {key} : {value}", end=",  ")
"""





# practice proble 3:
"""
# this two must be stored outd=side of the whie loop, otherwise they will reset to an emptry list in each itteration
uins =[]
grades = [] #grade and uin have the same index

while True:
    try:
        uinGrade = input("enter your uni and then grade (q to quit) : ")
        if uinGrade == "q":
            break
        uinGradeLst = uinGrade.split(" ")
        uins.append(uinGradeLst[0])
        grades.append(int(uinGradeLst[1])) # make sure to convert it into a number
    except:
        print("please enter only digits")


totalDict = {} # { key:[value1, value2, value3,...], }

for i in range(len(uins)):
    uin = uins[i] # will be a key
    grade = grades[i] # will be a value
    if uin in totalDict.keys() : #if the key exist in the dictionary it return true
        totalDict[uin].append(grade)
    else: #if the key:value pair don't exist in the dictionary
        totalDict[uin] = [grade] #creating a list with a value inside

for key in totalDict.keys():
    valueCount = len(totalDict[key])
    totalValue = sum(totalDict[key])
    maxValue = max(totalDict[key])
    minValue = min(totalDict[key])
    averageValue = totalValue / valueCount
    # then lets print the output
    print(f"{key}: ")
    print(f" Max: {maxValue}, Min: {minValue}, Avg: {averageValue}")
"""




# this two must be stored outd=side of the whie loop, otherwise they will reset to an emptry list in each itteration
uins =[]
grades = [] #grade and uin have the same index

while True:
    uinGrade = input("enter your uni and then grade (q to quit) : ")
    if uinGrade == "q":
        break
    # add conditions to check it is all numbers and the1st and last number of uin is != 0
    uinGradeLst = uinGrade.split(" ")
    uins.append(uinGradeLst[0])
    grades.append(int(uinGradeLst[1])) # make sure to convert it into a number

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




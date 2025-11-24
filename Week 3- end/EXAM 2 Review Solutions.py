
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

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dawit Abebe Tenagne
# Section: 556
# Assignment: 1.12.1: LAB
# Date: 11/05/2025
#
#
# YOUR CODE HERE

#File reading and handling part
try:
    filePath = input("Enter the name of the file: ")
    barcodeList = []
    file =  open(filePath, "r")
    for line in file:
        eachcode = line.strip() #remove all white space and newline character
        barcodeList.append(eachcode)
    file.close()
except FileNotFoundError:
    print("File can not be found")

validCodes = 0
validbarcodes = []
for barcode in barcodeList:
    # computational part for checking each barcode
    #barcode = 1877455846014
    group1 = []
    group2 = []

    for x in range(0,12): #12 or the las digit is excluded so we're good
        if x %2 == 0: ##for even index (0,2,4..) it give 1st,3rd,5th,7th...numbers = group1
            num1 = int(barcode[x])
            group1.append(num1)
        elif x%2 ==1: ## for odd index (1,3,5..) gives the 2nd,4th,6th number = 2nd group
            num2 = int(barcode[x])
            group2.append(num2)

    group1Sum = sum(group1)
    group2Sum = sum(group2)
    digit = (3*group2Sum) + group1Sum

    lastDigit = digit % 10
    checkingNum = 10 - lastDigit
    lastCode = int(barcode[12])

    if checkingNum == lastCode:
        validCodes +=1
        validbarcodes.append(barcode)
print(f"There are {validCodes} valid barcodes")

with open("valid_barcodes.txt", "w") as fileObject:
    for code in validbarcodes:
        fileObject.write(code + "\n")


#barcodes.txt
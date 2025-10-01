# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Dawit Abebe Tenagne
# Section: 556
# Assignment: 1.12.1: LAB
# Date: 01/10/2025
#
#
# YOUR CODE HERE

num = input("Enter numbers: ")

# changing the string list into integer list
numList = []
for i in num.split(" "):
    numList.append(int(i))

# defining  a function that sum up the total sum of a given list of integers and return the sum
def listSum(lst):
    total = 0
    for x in lst:
        total += x
    return total

# splitting the list using a for loop, unti their sum equals to one another
splitted = False
for j in range(1,len(numList)):
    # making the left list equal to the 1st element, and the right ther rest of the list
    leftList = numList[:j]
    rightList = numList[j:]
    #then if the sum of the sum equals i will just print the left and right list and break through this for loop
    # if the sum is not equal the left list will be numList[:2] the 1st and second element, and the right list will be the 3rd element upto the ned
    # then we continue until their sum equals one another
    leftSum = listSum(leftList)
    rightSum = listSum(rightList)
    if leftSum == rightSum:
        print("Left: ",leftList)
        print("Right: ",rightList)
        print(f"Both sum to {leftSum}")
        splitted = True

# if the for loop finished iterating and still don't meet the condition of my if statement ( which is leftsum = right sum)
# then i will print the error message
if not splitted:
    print("Cannot split evenly")
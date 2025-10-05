"""
# 6

num = "800-GOFEDEX"    #input("enter xxx-xxxxxxx : ")
numlist = num.split("-")
letters = numlist[1]
last7 = [] #[2,3,4,5,6,7,8]
for i in letters:
    last7.append(i)
for i in last7:
    if i.lower() in "abc":
        last7[last7.index(i)]= 2
    elif i.lower() in "def":
        last7[last7.index(i)]= 3
    elif i.lower() in "ghi":
        last7[last7.index(i)]= 4
    elif i.lower() in "jkl":
        last7[last7.index(i)]= 5
    elif i.lower() in "mno":
        last7[last7.index(i)]= 6
    elif i.lower() in "pqrs":
        last7[last7.index(i)]= 7
    elif i.lower() in "tuv":
        last7[last7.index(i)]= 8
    elif i.lower() in "wxyz":
        last7[last7.index(i)]= 9

print(f"{numlist[0]}-{last7[0]}{last7[1]}{last7[2]}-{last7[3]}{last7[4]}{last7[5]}{last7[6]}")"""


"""
# 8

num = int(input("enter b/n 100 and 1 million: "))
while num not in range(100,1000001):
    print("input error")
    num = int(input("enter b/n 100 and 1 million: "))
ones = num % 10
tens = (( (num%100) - (num%10) )/10)

if ones % 2 ==0 and tens % 2 ==0:
    print("both are even")
    print(f" sum = {ones + tens}")
elif ones % 2 == 1 and tens % 2 == 1:
    print("both are odd")
    print(f"product = {ones * tens}")
else:
    print("one is odd, one is even")"""


"""
# 9
num = int(input("enter number: "))
n = str(num)
nn = str(num) + str(num)
nnn = str(num) + str(num) + str(num)
sum = int(n) + int(nn) + int(nnn)
print(f"{n} + {nn} + {nnn} = {sum}")
"""



"""
# 10
word = input("enter text: ")
for x in range (1,len(word)+1):
    print(word[-x],end="")
"""




"""
#11

print("---------------------------------------------")
print("Integer Multiples")
print("---------------------------------------------")

for n in range(2, 6):
    print(n, end="         ")
    for x in range(n, (n*10)+1):
        if x / n == 10:
            print(x)
        elif x % n ==0:
            print(x, end=", ")
    print()
print("---------------------------------------------")
"""





"""
#12

num = int(input("enter number: "))
numString = str(num)
sum = 0
for x in numString:
    sum += int(x)
print(f" sum of digits: {sum}")
"""

"""
#13
print("Enter 5 items and their cost")
Item1 = input("Item 1:").split(" ")
Item2 = input("Item 2:").split(" ")
Item3 = input("Item 3:").split(" ")
Item4 = input("Item 4:").split(" ")
Item5 = input("Item 5:").split(" ")
money = float(input("How much money to you have"))

Items = [Item1,Item2,Item3,Item4,Item5] # [["apple", "0.5"], ["banana",0.5]...]

affordable = []
for row in Items:
    if float(row[1]) <= money:
        affordable.append(row[0])
print(f"you can afford", end = " ")
for x in affordable:
    if x == affordable[-1]:
        print(f"or {x}",end=" ")
    else:
        print(x, end=", ")

"""



"""
#15
num = int(input("enter a number: "))
index1 = 0
index2 = 1
fibbonachi = [0,1]
if num == 0:
    print(0)
elif num >=1:
    nextNumber = 1
    while nextNumber <= num:
        fibbonachi.append(nextNumber)
        index1 +=1
        index2 +=1
        nextNumber = fibbonachi[index1] + fibbonachi[index2]
for number in fibbonachi:
    if number == fibbonachi[-1]:
        print(number) # if it is the las number just print the number without the comma ending
    else:
        print(number, end=", ")"""

"""
# 16

row = int(input("enter the number of rows: "))
column = int(input("enter the number of column: "))
list2D =[]
for x in range(row):
    innerList = [] #this will reset to empty list in every itteration
    for y in range(column):
        innerList.append(x + y)
    list2D.append(innerList)
print(list2D)
"""
"""
# 17

num = "1.2 3.4 5.6 7.8 123.456 102 8 6 7 5 3 0 9 -987.6"  #input("enter the numbers:")
numList = [float(x) for x in num.split(" ")]
sortedList = []

while len(numList) !=0:
    # want to itterate the below code until there is no element left in the numList
    # tip when you are doing tings that require nested itteration start with the inner loop and go outside
    lowest = numList[0] #assuming the 1st number is the lowest number
    for x in numList:#by itterating the below condition in every element we can get the lowest number
        if x < lowest:#check if x is the lower than the lowest number that is randomly assigned, if it is lower change it
            lowest = x
    sortedList.append(lowest)
    numList.remove(lowest)
    
print(sortedList)
print(f"second largest element = {sortedList[-2]}")"""

















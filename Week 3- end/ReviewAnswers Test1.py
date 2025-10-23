
#--------------------------from review video---------------------------------------------------

"""
#review QS
#repeatedlly adding digits of a number, until the sum becomes a single number

num = (input("enter the number: "))
digitsInteger = [int(x) for x in list(num)]
condition = True
while condition:
    digitsSum = sum(digitsInteger)
    #this is number so we have to convert it into string inorder to itterate over the digits, and then to integer to assign it to the digitsInteger again
    digitsSumString = str(digitsSum)
    digitsInteger = [ int(x) for x in digitsSumString ]
    if len(digitsInteger) == 1:
        finalSum = digitsSum
        condition = False
print(finalSum)
"""

"""
# review QS
word = (input("enter your words: ")).lower()
letters = list(word)
vowels = "aeiouyAEIOUY"
vowelLetters = []
count = 0

for x in letters:
    if x in vowels:
        vowelLetters.append(x)
        count +=1
print(f"there are {count} vowels: ", end=" ")
for x in range(len(vowelLetters)):
    if x == len(vowelLetters)-1:
        print(vowelLetters[x], end=" ")
    else:
        print(vowelLetters[x], end=", ")"""

"""
# review question 
#finding the intersection of a list

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
intersection = []

for x in list1:
    for y in list2:
        if x == y:
            intersection.append(x)

print(intersection)
"""

"""
# review question
# reversing the word

word = input("enter the word: ")
reversedWord = word[::-1]
print(reversedWord)
"""

"""
# review question
# reversing the word without using indexing []

word = list(input("enter the word: "))
reversedWord = []

for x in word:
    reversedWord.insert(0,x)
print("".join(reversedWord))
"""
#-------------------------------------------------------------------------------



"""
for x in range(1,6):
    print(chr(96+x)*x)
print()
print("---------------------------------")
print()
for x in range(1,6):
    if x <=3:
        print(">"*x)
    else:
        print(">"*(6-x))

print()
print("---------------------------------")
print()

for x in range(1,6):
    if x <=3:
        print("x"*(4-x))
    else:
        print("x"*(x-2))

print()
print("---------------------------------")
print()
for x in range(1,6):
    print(" "*(x-1) + "o"*(6-x))

print()
print("---------------------------------")
print()
for x in range(1,6):
    print("x"*(5-x) +"o"*(x-1))


"""

"""
condition = True
ageList = []
count = 0
while condition:
    age = int(input("enter age: "))
    if age<0:
        condition = False
    else:
        ageList.append(age)
        count +=1
maxAge = max(ageList)
minAge = min(ageList)
print(f" no : {count}, max: {maxAge}, min: {minAge}")"""




"""
# 7

num = "800-GOFEDEX"    #input("enter xxx-xxxxxxx : ")
numlist = num.split("-")
letters = numlist[1]
last7 = [] #[2,3,4,5,6,7,8]
for i in letters:
    last7.append(i)
for i in last7: #i = element ( not index!!!)
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




# 10
"""
word = input("enter text: ")
for x in range (1,len(word)+1):
    print(word[-x],end="")
"""
#✅




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
#14
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
# row = [0,1,2]
# column = [0,1,2,3]

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
    
    lowest = numList[0] #assuming the 1st number is the lowest number
    for x in numList:
        if x < lowest:
            lowest = x
    sortedList.append(lowest)
    numList.remove(lowest)
    
print(sortedList)
print(f"second largest element = {sortedList[-2]}")"""


"""
# 18
#my algorithm :) since we can itterate through a string -> itterate through it assign the 1st element and then immediatly braek out of the loop

word = input("Enter a word: ")
count = 0 
firstword = word
firstletter = firstword[0]
while word.lower() != "stop":
    count += 1
    word = input("enter another letter: ")
    anotherfirst = word[0]
    if anotherfirst < firstletter:
        firstletter = anotherfirst
        firstword = word
print(f"If these {count} words were to be sorted alphabetically, the first word would be '{firstword}'")"""




"""


#19
# you can't convert string of numbers separated by space directly into a number using int() or float() !!!
# ex. int("12 34 67 54 355") = error, int("12 34 67 54 355".split(" " ) = error = same shit.
# same apply to float:- float("12 1234 13 12") = float("14,56,79,54,24".split("")) = error

num = input("enter number: ").split(" ")
numList = []
for x in num:
    numList.append(int(x))
duplicates = False
for x in numList:
    occurance = numList.count(x)
    if occurance > 1:
        duplicates = True
if duplicates == True:
    print("duplicates")
else:
    print("all unique")"""



"""
#20

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))
while num2 < num1:
    print(" number 2 should be greater than number")
    num2 = int(input("enter number 2: "))

sum = 0
for x in range(num1, num2 + 1):
    if x %4 ==0:
        sum += x
print(f"the sum of the multiples of 4 bitween {num1} and {num2} is {sum}")"""









"""
#21

nameList = []
ageList = []
#name and age of the person in the bellow list will have the same index number
#b/c bothe are appended at the same time

condition = True
while condition:
    nameAge = (input("enter the name and age. ex, Ritchey 39, enter: baby 0 to exit : ")).split(" ")
    name = nameAge[0]
    age = int(nameAge[1])
    if age == 0:
        condition = False
    else:
        nameList.append(name)
        ageList.append(age)

maxAge = max(ageList)
minAge = min(ageList)
totalAge = sum(ageList)
totalPeople = len(nameList)
averageAge = totalAge / totalPeople
youngestPerson = nameList[ageList.index(minAge)]
oldestPerson = nameList[ageList.index(maxAge)]

print(f"The average age is {averageAge}")
print(f"{oldestPerson} is the oldest at {maxAge}")
print(f"{youngestPerson} is the youngest at {minAge}")
"""

"""
#22
# setting variables

total = 0
count = 0
max = None
min = None

condition = True

while condition:
    num = float(input("enter the number: "))
    if num < 0:
        condition = False
    else:
        count +=1
        total += num

        # at the first value both max and min will be the same because we only have one number yet
        if max == None or num > max:
            max = num
        if min == None or num < min:
            min = num

if count > 0:
    average = total/count
    print(f" max : {max}, min : {min}, average : {average}")
else:
    print("you have entered only a negative number")
"""





"""
#23

from math import *
area = float(input("enter the value of the area: "))
radius = sqrt(area/pi)
side = sqrt(area)
print(f" circle with area {area} has a radius: {radius:.1f}")
print(f"square with area{area} has a side length: {side:.1f}")"""


"""
#24

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
while num2 < num1:
    print("num2 should be greater than num1")
    num2 = int(input("enter num2: "))
multiples = []
for x in range(num1, num2 + 1):
    if x%5==0 and x%7==0:
        multiples.append(x)

print("multiples :", end=" ")
for x in multiples:
    if x == multiples[-1]:
        print(x)
    else:
        print(x, end=", ")"""








"""
#25

list_words = ["abc","df","edefjf","gjbjvbhe","sddvjbvvbvh","bubvweiwi","d","ss","a","abcdefghigklmnop"]
word = None
longestLength = 0
for x in list_words:
    if longestLength == 0 or len(x) > longestLength:
        longestLength = len(x)
        word = x
print(f"the longeth word is {word} and has {longestLength} number of characters")
"""




"""
#26
#" "[start:end:step] can also be applied to a string 🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
sentenceList = input("enter the sentence: ").split(" ")
print("words reversed:", end=" ")
for x in sentenceList:
    print(x[::-1], end=" ")
"""


#27 = skipped


#28  = skipped
"""
#29

xdata = [0, 1, 2, 3, 4, 5]   
ydata = []
for x in xdata:
    y = 4.12 * x**2 + 1.52 * x - 7.1
    ydata.append(y)
print("xdata:", xdata)
print("ydata:", ydata)
"""

#30
""" #for checking 1 number if its prime
num = int(input("enter number: "))
prime = True
for x in range(2,num):
    if num %x==0: #if the number is divisible by any number except 1 and itself = then itr is not a prime
        prime = False
if prime:
    print(num,"is prime")
else:
    print(num, "is not prime")


# for checking range of numbers if they are prime just nest the previous checking inside another loop
# to check numbers b/n 1 and 72
primes = []
count = 0

for num in range(1,73):
    prime = True

    for x in range(2,num):
        if num % x == 0: 
            prime = False

    if prime:
        primes.append(num)
        count +=1

print(count)
print("primes: ", primes)
"""


"""
#31

mass = input("enter mass: ").split(" ")
volumes = input("enter volume: ").split(" ")
massList = [float(x) for x in mass]
volumesList = [float(x) for x in volumes]
densityList = []
for x in range(len(massList)):
    density = massList[x]/volumesList[x]
    densityList.append(density)
for x in  densityList:
    print(x, end=",")
"""

#32 = skipped
"""
# Ask the user for the 4-digit combination
lock_number = input("Enter a 4-digit combination: ")

# Store the combination as a 2D list (list of lists)
lock = [[int(digit)] for digit in lock_number]

print("The lock is stored as:", lock)

# Variable to count how many tries it takes
tries = 0

# Try every possible 4-digit combination
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                tries += 1
                guess = [[a], [b], [c], [d]]

                # Check if the guess matches the lock
                if guess == lock:
                    print("Lock solved!")
                    print("The combination is:", a, b, c, d)
                    print("Total tries:", tries)
                    break
            else:
                continue
            break
        else:
            continue
        break
"""


"""
#33

from math import *
r = float(input("enter the radius: "))
area = pi * (r**2)
perimeter = 2*pi*r
lengthArea = sqrt(area)
lengthPerimeter = (perimeter / 4)

print("area", area)
print("perimeter", perimeter)
print("length from Area", lengthArea)
print("length from Perimeter", lengthPerimeter)"""


#--------------------more QS------------------------------------------------------------------------
"""
hashardno = []
count = 0
for x in range(1,100):
    num1 = x//10
    num2 = x %10
    sum = num1+num2
    if x % sum == 0:
        count +=1
        hashardno.append(x)
print(count)
for x in hashardno:
    print(x, end=", ")"""




#-------------------------------------------------------------



"""
#lab7: Dropping the 1st consonant
name = input("enter ur name: ")
vowel = "aeiouyAEIOUY"
ame = None

for x in range(len(name)):
    if name[x] in vowel:
        ame = name[x:]
        break
print(f"..rhyme....{ame}.....rhyme" )
"""



"""
#lab7: splitting list




num = input("enter numbers separated by space: ").split(" ")
numList = [ int(x) for x in num]
left =[]
right = []
leftSum = None
rightSum = None
for x in range(1,len(numList)):
    left = numList[:x]
    right = numList[x:]
    leftSum = 0
    rightSum = 0
    for x in left:
        leftSum += x
    for y in right:
        rightSum +=y
    if leftSum == rightSum:
        break
if leftSum == rightSum:
    print("left:", left )
    print("right:", right)
    print("sum:", leftSum)
else:
    print("can't split")"""


"""
#lab 6 part 1
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
for x in range(1,101):
    if x % num1 == 0 and x % num2 == 0:
        print("howdy whoop")
    elif x % num1 == 0:
        print("howdy")
    elif x % num2 == 0:
        print("whoop")
    else:
        print(x)"""
"""
#lab 6 part 2
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
while num2 < num1:
    print("num2 should be greater than num1")
    num2 = int(input("enter num2: "))
sum = 0
for x in range(num1, num2+1):
    sum +=x
print(f" sum b/n {num1} and {num2} is {sum}")"""



"""
#lab 6 part 2, juggler sequence

from math import *

num = int(input("enter num: "))
juggler = []
juggler.append(num)

while num != 1:
    if num % 2 ==0:
        num = floor(sqrt(num))
    elif num % 2 == 1:
        num = floor(num ** (3/2))
    juggler.append(num)
for x in range(len(juggler)):
    if juggler[x] == juggler[-1]:
        print(juggler[x])
    else:
        print(juggler[x], end=", ")"""




"""
#27
from math import *
x= float(input("enter the number b/n -1 and 1: "))
while not(-1<x and x <1):
    print(" x should be  b/n -1 and 1")
    x = float(input("enter the number b/n -1 and 1: "))
sum = 0
power = 1
denominator = 1
condition = True

while condition:
    term = (2/denominator) * ( x ** power)
    if abs(term) > ( 10 ** (-6)):
        sum += term
        denominator +=2
        power +=2
    else:
        condition = False
print(f" ln(1+x) - ln(1-x) is approximatly {sum}")"""




"""
#28

x = float(input("enter the number b/n -1 and 1: "))
while not (-1<x and x<1):
    print("x should be b/n -1 and 1")
    x = float(input("enter the number b/n -1 and 1: "))

power = 0
sum = 0
condition = True

while condition:
    term = (x ** power)
    if term > (10**(-6)):
        sum += term
        power +=1
    else:
        condition = False
print(sum)"""







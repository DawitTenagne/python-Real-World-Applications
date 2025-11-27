
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
# ✅ already done but u can do it again






#✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅

# 55
"""
months = { "January": 1, "February": 2, "March": 3,
           "April": 4, "May": 5, "June": 6, "July": 7,
           "August": 8, "September": 9, "October": 10,
           "November": 11, "December": 12 }

birthSorted = [] #[ [12,12],[1,15],[4,12] ]
for i in range(1,6):
    birthday = input(f" user{i} enter your birthday: ").split() # ["april',"14"]
    day = int(birthday[1])
    monthNum = months[birthday[0]]
    lst = [monthNum, day]
    birthSorted.append(lst)
birthSorted.sort()

#change back to month name after sorting
for key in months.keys(): # loop through each key in the dictionary
    for birth in birthSorted: #loop through each month in the birthday
        if birth[0] == months[key]: # if the month number and the key value math, assign the key instead of the number
            birth[0] = key

for birth in birthSorted:
    print(f"{birth[0]} {birth[1]}")
"""

#56
"""
phoneNo = input("Enter a phone number in this format XXX-XXXXXXX: ")
phone = phoneNo.split("-") # ["800","GOFEDEX"]
first3 = int(phone[0]) #800
last7 =list(phone[1]) # ["G","O","F","E","D","E",X"]
phonedict = {2:["A","B","C"],3:["D","E","F"],
             4:["G","H","I"],5:["J","K","L"],
             6:["M","N","O"],7:["P","Q","R","S"],
             8:["T","U","V"],9:["W","X","Y","Z"]}

for key in phonedict.keys():
    for i in range(len(last7)):
        if last7[i] in phonedict[key]:
            last7[i] = key

print(f"{phoneNo} is equivalent to", end=" ")
print(first3,end="-")
for i in range(len(last7)):
    if i == 2:
        print(last7[i],end="-")
    print(last7[i],end="")
"""

#57
"""
patients = int(input("Enter the number of patients: "))
patientDict = {}
for i in range(patients):

    info = input("Enter the next name and information: ").split(" ")
    # ["Amari","120/75","78","102"]
    name = info[0] # "Amari"
    status = info[1:] # ["120/75","78","102"]
    patientDict[name] = status
pName = input("Enter a name:")
if pName in patientDict:
    print(f"Here is information on {pName}:")
    print(f"Blood pressure:{patientDict[pName][0]}, pulse: {patientDict[pName][1]}, Blood glucose: {patientDict[pName][2]} ")
"""


#58
"""
def numcondition(x,y):
    #add docstring to explain the function
    '''If the integers add to more than 10 and multiply to more than 20,
    return True. If neither condition is satisfied, return False.
    If one condition is satisfied, return which condition'''

    if (x+y > 10) and (x*y >20):
        return True
    elif (x+y > 10):
        return "addition only"
    elif (x*y >20):
        return "multiplication only"
    else:
        return False

print(numcondition(3,7))
"""

#59
"""
# the module code
def isprime(num):
    '''The function isprime() takes in as a parameter a
    single integer, and returns either True or False.'''
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    return prime
    """

"""
# the solution code

from ENGR102 import isprime

while True:
    try:
        x = int(input("Enter an integer: "))
        y = int(input("Enter another integer:"))
        break
    except:
        print("Bad input! Try again")

primes = []

if isprime(x):
    primes.append(x)
if isprime(y):
    primes.append(y)

for i in range(x+1,y): #we already checked x and y, so we have to exclude them
    if i %2 ==1:
        if isprime(i):
            primes.append(i)
if len(primes) == 0:
    print("No primes found!")
else:
    print(f" Primes: {primes}")
    """


#60


"""
def max_min(a,b,c,d,e,f):
    '''this function returned reversed list, sum, and number of evens'''
    lst = [a,b,c,d,e,f]
    lst.sort(reverse=True)
    lstSum = sum(lst)
    evenCount = 0
    for i in lst:
        if i %2 == 0:
            evenCount +=1
    return (lst,lstSum,evenCount)

print(max_min(1, 6, 2, 5, 3, 4))
"""


#61

"""
import numpy as np

def matrixMult(arr1,arr2):

    ''' return the matrix operation of 2 array 
    if they match their inner dimension (shape)'''
    
    shape1 = arr1.shape #(a,b)
    inner1 = shape1[1]   #b
    shape2 = arr2.shape  #(c,d)
    inner2 = shape2[0]  #c
    if inner1 == inner2:
        arr3 = arr1 @ arr2
    else:
        arr3 = np.array([])
    return arr3


a = np.array([[0,1,2], [3,4,5]])
b = np.array([[0,1,2,3], [4,5,6,7], [8,9,10,11]])
matrixMult(a, b)

"""

#62

"""
def myinsert(string, char):
    '''insert a character in a string, maintaing the sort'''
    lst = list(string)
    for i in lst:
        if char < i:
            indx = lst.index(i)-1 #1 index back from the character
            lst.insert(indx,char)
            break #once added break out of the forloop
        else: # if the character is greater than every element, just append it at the ned
            lst.append(char)
            break #once added break out of the forloop
    str = "".join(lst)
    return str

print(myinsert("abde", "c"))
"""

#63
"""
def menVar(lst):
    n = len(lst)
    series1 = 0
    for i in lst:
        series1 += i
    mean = series1 / n
    series2 = 0
    for i in lst:
        series2 += (i-mean)**2
    variance = series2 / (n-1)
    return (mean, variance)

def menVar(lst):
    arr = np.array(lst)
    men = np.mean(arr)
    var = np.var(arr)
    return (men, var)
"""

#64

"""
while True:
    try:
        x = int(input("Enter an integer:"))
        y = int(input("Enter another integer:"))
        if x>0 and y>0:
            break
        else:
            print("We need a positive integer, try again")
    except:
        print("Bad input! Try again")

def armStrong(a,b):
    armStrongLst = []
    for i in range(a, b+1):
        lst = list(str(i))  # 234--> ["2","3","4"],    1-->["1]
        numDigit = len(lst) # number of digit
        total = 0
        for j in lst:
            total += (int(j)**numDigit)
        if total == i:
            armStrongLst.append(i)

    return armStrongLst

print(armStrong(x,y))
"""


#65

"""
while True:
    try:
        n = int(input("Enter an integer:"))
        if n>0:
            break
        else:
            print("Need a positive integer:")
    except ValueError:
        print("Bad input! Try again")

def perfectNum(num):
    divisors = []
    for i in range(1,num): # we don't count the number it self as the divisor
        if num % i == 0:
            divisors.append(i)
    total = sum(divisors)
    if total == num:
        return True
    else:
        return False

if perfectNum(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
"""

#66


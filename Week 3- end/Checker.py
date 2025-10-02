
# calculating the factorial of a given number

N = int(input("enter the number: "))
i = 1
f = 1
while not i > N:
    f= f*i
    i +=1
print(f)
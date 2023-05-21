import math

def fact1(num):
    return  math.factorial(num)

def fact2(num):
    fact=1
    for i in range(1,num):
        fact+=fact*i
    return fact

def fact3(num):
    if (num==1):
        return num
    else:
        return num*fact3(num-1)

5
print(fact3(5))
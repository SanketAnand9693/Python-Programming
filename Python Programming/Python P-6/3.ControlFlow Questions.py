'''
#Program for larger number
a,b=int(input("enter a")),int(input("enter b"))
if a>b:
    print('a is greater than b')
if a<b:
    print('b is greater than a')

#program to check number is positive or not
a= int(input('Enter a value'))
if a>0:
    print(f"the number {a} is positive ")

#Program to check number is greater than 10
a= int(input('Enter a value'))
if a>10:
    print(f'the value {a} is greater than 10')
else:
    print(f" the {a} is not greater than 10")

#Number even or odd
a=int(input("Enter a number:"))
if a%2==0:
    print(f'the value {a} is even')
else:
    print(f'the value {a} is odd')

#Program to check the is divisible by 5
a=int(input("Enter a value"))
if a%5==0:
    print(f"the value {a} is divisible by 5")
else:
    print(f'{a} not divisble by 5')

#Compare two numbers
a= int(input('Enter a value'))
b= int(input('Enter a value'))
if a==b:
    print(f'the value {a} and {b} are equal')
else:
    print(False)

#Print ascending and descending order of 3 numbers

a=int(input('enter value a'))
b=int(input('enter value b'))
c=int(input('enter value c'))
if (a<b) and (a<c):
    if b<c: print(f'{a},{b},{c}')
    else: print(f'{a},{c},{b}')
if (b<a) and (b<c):
    if a<c: print(f'{b},{a},{c}')
    else: print(f'{b},{c},{a}')
if (c<a) and (c<b):
    if a<b: print(f'{c},{a},{b}')
    else: print(f'{c},{b},{a}')

#Print grade based on the marks of student
a = int(input())
if (a)>=85:
    print("A+")
if (a)>=75 and a<85:
    print("B+")
if (a)>=65 and a<75:
   print('C+')
if (a)>=55 and a<65:
    print('D+')
'''
# PROGRAM FOR QUADRATICS EQUATIONS
import math
a =12
b=32
c=56
d=math.sqrt(b**2-4*a*c)

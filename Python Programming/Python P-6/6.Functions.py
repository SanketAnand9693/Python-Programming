#Functions
#Addition through function
"""def sum(a,b):
    return a+b
print(sum(1,2))
print(sum(6,2))
print(sum(6,5))"""

"""def functionname():
    #body of function
functionname() # calling of function
"""

#non parametrize
#parametrize

#performing a task only/ Returns a value
"""def greet():
    return "good evening!"
x=greet()
print(x, input())
"""
#returning a value  #Non parametrize function
"""def TakeInput():
    return int(input("enter a value"))
y= int(input("enter"))
z=TakeInput()*y
print(z)"""

#Parametrize function
"""def sum(x,y): # by using x, y we give parameter to the function
    return (x+y)
a=int(input("enter value 1:"))
b=int(input("enter value 2:"))
multiply=int(input())
sumres=sum(a,b)
res=sumres+,multiply
print(f"Sum{sumres}")
print(f"Multiply{res}")"""
#pure functions
# x=12
# def change():
#     x=10
# change()
# print(x)        #in this the output will be 12 because of pure function

#Impure functions
  # these functions are not primarily recommended
# x=12
# def change():
#     global x
#     x=10
# change()
# print(x)  #the output will be 10 because of global



#Return multiple values from a function
"""def dummy():
    x,y=10,15
    return x
print(dummy())"""

"""
def Data(name, age, batchcode='p6'):
    return f" Name is {name} and batchcode is {batchcode}"
a= Data(age= 12, name="john")
print(a)"""

"""def Calc(a,b):
    def Add(x,y):
        return x+y
    def Product(p,q):
        return p*q
    addres= Add(a,b)
    prores= Product(a,b)
    return f"Add is {addres} and product is {prores}"
res = Calc
hello = res(12,5)
print(hello)"""

#questions guess the number
#WAP to find the weather given number is positive or negative
#P.S try to chamge positve number into negative or vice versa
"""def positive_negative():
    if n<0:
        print("Negative",end="\n")
        print("Its positive value is:",~n+1)
    else:
        print("positive",end="\n")
        print("Its negative form is:", ~n + 1)

n=int(input())
positive_negative()
"""
#WAP to find the given no. is odd or even
"""def even_odd(num):
    if num%2==0:
        return "Its is even number"
    else:
        return "Its a odd number"
res=even_odd()
print(res)
"""
#WAP to find the first N(user input) natural number
#P.S without loop
"""def sum(num):
    return num*(num+1)//2
res=sum(n)
print(sum)"""

"""def sum(a,b):
    return a + b
x= int(input("enter a value 1" ))
y= int(input("enter a value 2"))
add = sum
double = add(x,y) * 2
print(double)"""
######################
# def checkPalindrome(num):
#     if str(num) == str(num[::-1]):
#         return True
#     else :
#         return False
#     pass
#statement/ expession
'''

if condition:
    #true stmt
else:
    # false

isValid= True # can also enter int,char

#simple if and else
if isValid:
    print("Logged in!")
else:
    print("invalid")


##########
a= int(input())
if a<0:
    print("negative integer")
if a>0:
    print("positve integer")

#Multiple if else
n= 0
if n>0:
    print("positive")
if n<0:
    print('negative')
else:
    print("zero")
#######################################
#Nested if else
n= 0
if n>0:
    print("positive")
    if n%2==0:
        print("even")
else:
    print('negative')
    if n%2!=0:
        print('odd')

#########################
#Ternery operator

n=7
if n>=1:
   # if n<=1:
   #     print("valid")
   #else:
   #    print("partial valid")
r= "valid " if n <=10 else "partial valid"
print(r)
'''
########
#find the larger number between three
a = 12
b = 1
c = 6
if a > b and a > c:                          # b<a>c:
    print(f'a is larger number')
elif b > a and b > c:
    print(f'b is larger number')
else:
    print(f'c is larger number')

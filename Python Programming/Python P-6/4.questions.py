#find the given no. is prime or not
# x = int(input("Enter a number: "))

# if(x==1):
#     print("Not a prime number")

# elif(x>1 and x<4):
#     print("It is a Prime number!")

# else:
#     i=2
#     count=0
#     while(i<x):
#         if(x%i==0):
#             count+=1
#             print(i,end=",")
#         i+=1
#     if (count>0):
#         print('\n'"Since the no. is divisible by above no. so it is Not a prime number.")
#     else:
#         print("It is a Prime number.")

#prime no. by using for loop
x = int(input("Enter a number: "))
if(x==1):
        print("Not a prime number")

elif(x>1 and x<4):
        print("It is a Prime number!")
count=0
for i in range(5,x+1):
    if(x%i==0):
        count+=1
        print(i,end=",")
        print("prime number")
        if (count>0):
            print('\n'"Since the no. is divisible by above no. so it is Not a prime number.")
    else:
            print("It is a Prime number.")



# #factorial
# a=int(input())
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
#     i+=1
# print(fact)
"""n=int(input())
f= 0
s= 1
print(f,s,end=" ",sep=" ")
while n-2>0:
    next= f+s
    print(next,end=" ")
    f=ss=next
    n-=1"""
"""x= int(input("enter the value"))
sum=0
for i in range(x):
    j=int(input())
    sum=sum+j
print(sum/x)
"""

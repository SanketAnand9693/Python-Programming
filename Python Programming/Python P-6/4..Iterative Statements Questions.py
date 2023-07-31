# s=input()
# digit=0
# alpha=0
# symbol=0
# #print(dir(s))
# #print(help(s))
# for i in s:
#     if i.isdigit():
#         digit+=1
#     elif i.isalpha():
#         alpha+=1
#     else:
#         symbol+=1
# print(f'digit is {digit} \nalpha is {alpha} \nsymbol is {symbol}')

#####################################################

# Arrange the strings characters such that lower case letter should come first
"""s= input("Enter input")
lower =""
upper =""
for i in s:
    if i.isalpha():
        if i.islower():
            lower = lower + i
        else:
            upper+=i
print(lower+upper)"""
"""
n = int(input("enter a value"))
temp=n
rev=0
while n > 0:
    rem=n%10
    rev= rev*10+rem
    n=n//10
print(f"reverse of {temp} is {rev}")
if temp==rev:
    print(f"given number is pallindrome")
else:
    print(f"given number is non pallindromic")"""

# s=int(input())
# sum=0
# while s>0:
#     rem=s%10
#     sum=sum=sum+rem
#     s=s//10
# print(f"sum is {sum}")
#write code for factorial
#write code for vowel finder
a= int(input)
i=0
while i>0:
    if a%i:
        print("the no is prime")
    else:
        print("not a prime no.")

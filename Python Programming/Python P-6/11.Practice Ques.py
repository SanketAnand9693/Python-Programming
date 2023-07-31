"""def maleFemale():
    x=input()
    if x=="male" :
        print ("sir")
    elif x=="female":
        print ("mam")
    else:
        print("error")
maleFemale()"""
#accept an integer and check whether it is an even number or odd
#accept name and age from the user. check if the user is a valid voter or not
     # valid- Hello shery, You are  a valid voter
     #invalid - Sorry Shery, you can't  cast the vote
"""def Vote():
    z=18
    x=input("Enter name")
    name=int(input("enter age"))
    if z>name:
            print(f"Sorry {x}, you can't  cast the vote")
    elif z<=name:
        print(f"Hello {x}, You are  a valid voter")
Vote()"""
#accept the corresponding number 1-7 and print the ocrresponding day
"""def day(x):
    if i in range(1,8):
        if i ==1: print("monday")
        elif i == 2: print("tuesday")
        elif i == 3: print("wednesday")
        elif i ==4: print("thursday")
        elif i ==5: print("friday")
        elif i ==6: print("saturday")
        elif i ==7: print("sunday")
i=int(input())
day(i)
"""

#leap year or not
"""x=int(input())
if x%4==0 and x%100==0:
    if x%100!=0 or x%400==0:
        print("leap year")
    else:
        print("not")
else:
    print("not")"""
"""
n=int(input())
for i in range(1,n+1):
    if n>0:
        print("hello World",i)
    n+=1"""
#++++++++++++++++++++++++++++++++++++++++++++++++++++
#print natural number upto n
# n=int(input())
# for i in range(1,n+1):
#     print(i)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
# reverse printing of natural number
# for i in range(n,0,-1):
#     print(i)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
# n=int(input())
# for i in range(1,11):
    # print(n,"*",i,"=",n*i)
# for i in range(1,11):
#     x=(i*i+1)
# print(x)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#factorial of number
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
#++++++++++++++++++++++++++++++++++++++++++++
# sum_even=0
# sum_odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum_even=sum_even+i
#     else:
# print(sum_odd)
# print(sum_even)
# #+++++++++++++++++++++++++++++++++++++++++++++
# for i in range(1,n+1):
#     if i%3==0:
#         print(i)
#     elif i%5==0:
#         print(i)
#
def count_substring(string, sub_string):
    count=0
    for i in string:
        for j in sub_string:
            for sub_string in string:
                count=count+ 1
        i+=1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
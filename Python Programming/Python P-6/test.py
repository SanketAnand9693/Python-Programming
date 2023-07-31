"""x=input("enter 1st word")
# y=input("enter 2nd word")
# z=input("enter 3rd word")
# print(z.upper())
for i in x:
  if i=="a" | i=="e" | i=="o" | i=="u" | i=="i":
      x1=i.replace("*")
      i+=1
print(x)"""
#ques no.4
"""x=int(input("no. of people"))
z=0
for i in range(1,x):
    if x>0:
        H=x-i
        z=H+z
print(z)
"""


# list comprehension hackerrank
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     set1=[]
#     set2=[]
# for i in range(0,x+1):
#     if i<=x:
#         for j in range(0,y+1):
#             if j<=y:
#                 for k in range(0,z+1):
#                     if k<=z:
#                         if i+j+k!=n:
#                             set2.append(i)
#                             set2.append(j)
#                             set2.append(k)
#                             L=[i,j,k]
#                             set1.append(L)
# print(set1)

##########################################################
# string=input()
# sub_string=input()
# a=[]
# count=0
# for i in range(0, len(sub_string)):
#     print (sub_string[i])
# for j in range(0,len(string)):
#     if j==i:
#         j.append(a)
#         if a==string:
#             count=count+1
#     else:
#         pass
#     count=count+1
# print(count)
##########################################
#fibonacci series for list or array
# n= 10
# fibo=[0,1]
# for i in range(2,n):
#     c=fibo[i-2]+fibo[i-1]
#     fibo.append((c))
# print(fibo)

#######################################
# l=[]
# positive=[]
# negative=[]
# l=[3,67,34,-56,32]
# for i in l:
#     if i>=0:
#         positive.append(i)
#     else:
#         negative.append(i)
# print("negative",sorted(negative))
# print("positive",sorted(positive))
#######################################################################
# n = int(input())
# s = []
# for i in range(1, 10):
#     s.append(i)
#
# print(set(s))
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     c=student_marks[query_name]
#     per=0
#     for i in c:
#         per=(per+i)
#     percentage=per/len(scores)
#     print(c)
#     print(percentage)

# print("{:.2f}".format(per))
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# sub_string=list("cdc")
# string=list("abcdcdc")
# count=0
# flag=False
# for i in string[0:len(string)]:
#     print("Sanket",i)
#
#     for j in sub_string[0:len(sub_string)]:
#         print("anand",j)
#         if i!=j:
#             break
#         if i==j:
#             flag=True
# if flag==True:
#     count+=1
# print(count)
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input())
print(fact(n))

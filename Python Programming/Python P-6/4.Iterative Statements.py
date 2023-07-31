#IN python there is entru control loops
#In python there is no switch
#there is no  do  while loop



#entry control -> while and for
#loop variable
#test condition
#update exp.
#body of loop
# we use for loop when we know start  and ending
# in sequential data type we can use directly use for loop
'''
for i in range(1, 11, 1):# (start , end +1, step)
    print(f"{i} - hello")
# reverse
for i in range(10, 0, -1):# (start , end +1, step)
    print(f"{i} - hello")

#strings
s= "john Doe"
for i in s:
    print(i)



#while loops
i =1
while i <11:
    i+=1
    print(f'{i}--Hello!')
'''
"""#
s="John Doe"
i=0
while i<len(s):
    print(f"{s[i]} -- Hello!")
    i+=1
##########################################
for i in range(1,11):
    if i%5==0:
        continue     #continue is basically like skip statment      #pass is for not process
    print(i,"iterating")
#######################################################
x= input()
for i in x:
    if i=='a' or i=='i' or i=='o' or i=='e' or i=='u':
        continue
    print(i,end=" ")"""
#####################################
"""
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiple is 23.
# find the sum of all the multiples of 3 and 5 below 1000.
sum=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)"""
"""sum=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)"""



################
"""BITWISE OPERATOR
~ complement
&= And operator
^= XOR"""
# for example complement of 5 is -6
# print(12|13)   # &= and ,|= or
#Examples of OR, AND, XOR
"""
#XOR
print(54|29)
print(54&29)
print(29^29)"""

#####################################33
"""Left shift & Right shift"""
"""print(5<<2) # here 2 is the  number of binaries to shift before decimal
print(173>>3) # here 3 is the  number of binaries to shift after the decimal"""

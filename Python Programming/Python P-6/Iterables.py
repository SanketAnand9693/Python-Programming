# l=[324,65,43,76]
# x=iter(l)
# print(l)
#for right angle triangle

"""
*
* *
* * *
* * * *
* * * * *
"""
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
###########################
#for print
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
 """
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
###############################
# A
# A B
# A B C
# A B C D
# A B C D E
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()

###################################
"""
* * * * * 
* * * * 
* * * 
* * 
* 
"""
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print("*",end=" ")
#     print()
#########################
"""
_ _ _ _ * 
_ _ _ * * 
_ _ * * * 
_ * * * * 
* * * * * 
"""
# for i in range(1,6):
#     for j in range(5,i,-1):
#         print("_",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
##########################################

# *
# **
# ***
# ****
# *****

"""for i in range(1,6):
    for j in range(1,i+1):
        print(i, end="")
    print()"""

# 1
# 22
# 333
# 4444
# 55555
# x=int(input())
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print(i, end="")
#     print()

#
"""for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()"""
"""for i in range(5,0,-1): # loop is in reverse
    for i in range(1,i+1): # i+1 is use because of
        print("*",end="")
    print()"""
########################
#without reversing loop only inner loop is reverse
"""for i in range(0,5): # loop is in reverse
    for i in range(1,6-i): # i+1 is use because of
        print("*",end="")
    print()"""

#mirror
"""for i in range(1,6):
    for k in range(1,6-i):
        print(" ", end="")
    for j in range(1,i+1):
        print("*",end="")
    print()"""
#Diamond printing
"""for i in range(1,6):
    for k in range(1,6-i):
        print(" ", end="")
    for j in range(1,i+1):
        print("*",end="")
    for i in range(1,i):
        print("*", end="")
    print()"""

# l=[234,56,897,45,67,789,988]
# x=map(lambda i:i%2==0,l)
# x=[i**2 for i in l]
# x=filter(lambda i:i%2==0,l) #for getting the value
# print(list(x))
############################################
# def names():
#     return "john"
#     return "jon"
#     return "jn"
#     return "j"
# print(names())
################################################
#for making generator replace return with yield
# def names():
#     yield "john"
#     yield "jon"
#     yield "jn"
#     yield "j"
# print(type(names()))
################################################

# from timeit import timeit
# from sys import getsizeof
# l=[i for i in range(1000000)]
# t=(i for i in range(1000000))
# print(getsizeof(t))
# print(timeit(t))
###########################################
#for combining two list we use zip
# l=[234,56,678,56,343,2,211]
# l1=(2,5,6,7,3,2)
# x= zip(l,l1)
# print(list(x))
############################################



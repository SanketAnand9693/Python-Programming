l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     l2.append(i*2)
# l2=[i*2 for i in l]  # in this the multiplication of 2 is print in list
#return exp for var in seq
# l2=[i for i in l[::-1]] # this is for reverse of list
l2=[i*2 for i in l if i%2==0] # for filtering the value for only print
print(l,l2)
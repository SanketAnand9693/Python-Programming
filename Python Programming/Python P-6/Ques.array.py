#how to take multiple input from the user
from array import array
x=int(input("enter the length"))
arr= array('i',[])
for i in range(x):
    arr.append(int(input("value")))
print(arr)

#Dictionary
# d={ }       #JSON= JavaScript Object Notation
# print(type(d))
d= {"key": "value","key":"value"}
d= {
    "name": "Sanket",
    "age": 21,
    "batch": "p6"
}
# res=d["name"]
# #updation
# """d["job status"]="private"
# print(d)"""
# # print(res)
# #Deletion
# del d["name"]
# print(d)

#clear
# d.clear()
#copy for sequential data type
# e=d.copy()
# print(e)
# for making dictionary from starts
# d= {
#     "name": "Sanket",
#     "age": 21,
#     "batch": "p6"
# }
# x=d.fromkeys(["a","b","c"], int(input()))
# print(x)
# # d.get is very imprtant because of it gives none if the parameter is not in the dictionary
# x= d.get("name")
# print(x)
#
# x= d.items()  # it is also a list of tuples
# print(x)
# #to get the keys including values
# for i in d.items():
#     print(i)
#
#
#
#note- .get does not break the program
# x= d.pop("name") # for deleting particular keys
# d.update({'age':45,'he':"ha"})          #for updation
# print(d)

##################################################
#######SET############################
# d=set()
# print(type(d))
# d={1,2,3,4,5,1,4,3,2,} # sets are collection of unique elements
# print(d)
natural={1,2,3,4,5,6,7,8,9}
whole={0,1,2,3,4,5,6,7,8,9}
even={2,4,6,8,10}
odd={1,3,5,7,9,11}
prime={2,3,5,7,11}
# s= set()
# s.add(12)
# ####
# s.pop()
# print(s)
s={12,23,54,645,3,2}
s.pop()
print(s)
#.discard() is used to    ???????????????
# .difference() is used to get the difference between the values
# .issubset() is used to check whether the values lies in the set
# x=natural.issuperset() is used    ?????????
# .union() makes the new set combining the two sets
# x= even | odd
# print(x)
x= prime ^ odd
print(x)

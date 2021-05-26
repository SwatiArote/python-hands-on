set1= {"111","222","222","333","1"}
print(set1) #no duplicates
print(set1.add("777")) #add in set
print(set1)
print(set1.remove("777"))
print(set1)
list1 = ["1", 22, "swati", 2.5, 2.5]
print(list1)
print("22" in list1)
print(set(list1)) #list to set
print(type(set(list1)))
print(set1 & set(list1)) #intersction
print(set1.union(set(list1))) #union
print(set1.difference(set(list1))) #union

set2= {"111","222","222","333","1", "379"}
print(set1.issubset(set2))
print(set2.issubset(set1))
print(set2.issuperset(set1))

#notes:
# A set is a unique collection of objects in Python.
# You can denote a set with a curly bracket {}. Python will automatically remove duplicate items

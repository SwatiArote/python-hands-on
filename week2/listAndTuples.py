#touple - are immutable
touple1 = ("hello", 1.5, -4) #sequenc
print(type(touple1))
print(touple1[0])
touple2 = touple1 + ('hii', -9, 6.7)
print(touple2)
print(len(touple2))
print(touple2[0:3])
touple3 = touple2 + (touple1, "nested") #netsed touple
print(touple3[-1])
print(touple3[-2][0])

#list - list r mutable
list1 = [1,2,3]
list2 = [1,2,3,[77,88]]
print(list2[3][1])
list3 = list2 + [90,100]
print(list3)
print(list1.extend([44,99])) #adds other list
list5 = list1.append([6,8]) #adds one element
print(list1)
print(list5)
list1[0] = 100
print(list1)
del(list1[2])
print(list1)
print("a,b,c,d".split(','))
alaisedlist = list2 #alaising
print(list2)
print(alaisedlist)
list2[0] = 5
print(list2)
print(alaisedlist)

#f we apply append instead of extend, we add one element to the list:
clonedList = list2[:] #cloning
print(list2)
print(clonedList)
list2[0] = 7
print(list2)

print(list2)
list2.pop(0)
print(list2)


#help command to get more
#help(list2)
# pop method removes  the elemet with given index
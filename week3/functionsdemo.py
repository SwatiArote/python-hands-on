list1 = [77,44,66,22,00,-67]
print(sorted(list1))
print(list1)
list1.sort()
print(list1)

#function
def add1(a):
    a = a+1
    return a

def mul(a,b):
    return a *b

def noReurn():
    pass
print(add1(5))
help(add1) #documentation
print(mul(2,3))
print(noReurn())
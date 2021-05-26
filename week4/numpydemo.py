import numpy
import time
import sys
import numpy as np

#numpy lib for sctific computaion
a= np.array([1, 2, 3, 4])
print(type(a))
print(a.dtype)
print(a.size)
print(a.ndim) #dimention of aaray
print(a.shape) #tuple indicates size of array in each dimention
print(a.std()) #std deviation
print(a[0])

#mododfy the values
print(a)
a[0] = 100 # new value for single value
print(a)
print(a[1:3]) #slicing
print(a)
a[1:3] = 200 , 300 # new values to slice
print(a)

#vector
u = [1,0]
v = [0,1]
z =[]
# traditional way for Vecor addition
for x,y in zip(u,v):
      z.append(x+y)
print(u)
print(v)
print(z)

# Vecor addition by numpy array
u = numpy.array([1,0])
v = numpy.array([0,1])
z = u + v
print(u)
print(v)
print(z)
print(u-v)

#Multiplying by scalar values
y = numpy.array([1,2])
z = 2*y
print(y)
print(z)

#Vector Product: hodomod product u o v
u = numpy.array([2,2])
v = numpy.array([3,2])
z = u * v
print(u)
print(v)
print(z)

#Vector Product: dot product u o v
# dot prodcut gives single result of addition of product of respective values
u = numpy.array([2,2])
v = numpy.array([3,2])
z = numpy.dot(u,v) # 2*2 + 3:2 =10
print(u)
print(v)
print(f"dot product of u n v: {z}")

#braodcasting
u = numpy.array([1,2,3,4])
print(u)
print(f"broadcasting of u(+1): {u+1}")

#universal funtions:
u = numpy.array([1,2,3,4])
print(u)
print(f"mean: {u.mean()}")
print(f"max: {u.max()}")
print(f"value of pi: {np.pi}")
vectorPi = np.array([0, np.pi/2, np.pi])
print(f"vector elemets: {vectorPi}")
print(f"sin of vector elemnts: {np.sin(vectorPi)}") #this will take sin of each elemet

#Linspace returns evenly spaced numbers over a specified interval.
#ploting number line
line = np.linspace(-2,2,5) #-2 is start, 2 is end, 5 is number of ssamples on line
print(line)
print(np.linspace(-2,2,9))
# line with pi functions
lineWithPi = np.linspace(0, 2*np.pi, 100)
print(lineWithPi)
lineWithPiBy2 = np.sin(lineWithPi)
print(f"sin of each elemet {lineWithPiBy2}")

# if to plot
# plt.plot(lineWithPi,lineWithPiBy2 )

#more links
#numpy.org

# Tow dimation arrays
list = [[11,11,11], [22,22,22], [33,33,33]]
twodarray = np.array(list)
print(twodarray)
print(twodarray.ndim) # gives the number of nested loops in array here tow list
print(twodarray.shape) #
print(twodarray.size) #
print(twodarray[0,1]) # 1st row, 2nd coloum
print(twodarray[0:2,1]) # for 2nd column row rang from 0 to 2

#matrix addition
x = np.array([[1,2],[2,1]])
y = np.array([[2,2],[3,1]])
print(x)
print(y)
print(f"matrix addition: {x+y}")
print(f"scalar multiplication of x with 2: {2 *x}")
print(f"Hadamard prodcut of x and y(elemet to elemet): {x * y}")
print(f"multiplication of x and y(no of colun in x should be same as rows in y): {x}")
# dot prodcut of row 1 to both column and dot predcut of 2nd row with both columsn

a = np.array([[1,2],[2,3]]) # of 2 * 2
b = np.array([[1,2,3], [2,1,2]] )# of 2 * 3  = a * b should be of 2 * 3
print(a)
print(f"matrxi:b : {b}")
print(f"transformed matrxi of b : {b.T}")

print(f"multiplication of a and b: {np.dot(a,b)}")

X = np.array([[1,0],[0,1]])
Y = np.array([[2,1],[1,2]])
print(np.dot(X,Y))

# 1 0    2 1
# 0 1    1 2
# 1*2 + 0*1  1*1 +0*2
# 0*2+1*1   0*1+1*2

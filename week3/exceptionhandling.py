
a = input("value of a: ")
b = input("value of b: ")

try:
    print(int(a)/int(b))
except :
    print("Cannot divdie by zero")
finally:
    print("done")


dist1 = {"1": 11, "2": 22, "3":33}
print(dist1["1"])
print(dist1.values())
print(dist1.keys())
print("1" in dist1)
print(11 in dist1)

#Keys can also be any immutable object such as a tuple:
# Keys can only be strings, numbers, or tuples, but values can be any data type.
print(range(5))
print(range(6,15))
squares = ["red","blue","white","green", "yellow", "white"]
print(squares)
#interating  elements
for square in squares:
    print(square)
# interating  index n elements
for i,square in enumerate(squares):
    print(i,square)


for i  in range(0,5):
    squares[i] = "white"
print(squares)

#while loop
colors = ["yellow","yellow","yellow","green", "yellow", "white"]
newSquare =[]
i =0
while(colors[i] == "yellow"):
        newSquare.append(colors[i])
        i= i+1

print(colors)
print(newSquare)


#notes:
 # range object as an ordered list.
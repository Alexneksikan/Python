startArray = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
newArray = [el for el in startArray if startArray.count(el) == 1]

print(startArray)
print(newArray)

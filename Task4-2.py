startArray = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Исходный список: {}'.format(startArray))

i = 0
outArray = []
while i < len(startArray) - 1:
    if startArray[i + 1] > startArray[i]:
        outArray.append(startArray[i + 1])
    i += 1
print('Результат в цикле     : {}'.format(outArray))

newArray = [startArray[i + 1] for i in range(0, len(startArray) - 1) if startArray[i + 1] > startArray[i]]
print('Результат в генераторе: {}'.format(newArray))

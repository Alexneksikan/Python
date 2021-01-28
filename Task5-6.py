fromFile = []
myDict = {}
with open("myFile6.txt") as myFile:
    content = myFile.readline()
    while content:
        print(content)
        fromFile.append(content.split())
        content = myFile.readline()

print('\n', fromFile)
for item in fromFile:
    sumItem = 0
    for j in range(1, 4):
        if any(map(str.isdigit, item[j])):
            sumItem += int("".join(filter(str.isdigit, item[j])))
    myDict[item[0]] = sumItem

print('\n', myDict)

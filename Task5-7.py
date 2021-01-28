import json

fromFile = []
goalArray = []
firmDict = {}
average_profit = 0
sum_profit = 0
n = 0

with open("myFile7.txt") as myFile:
    content = myFile.readline()
    while content:
        fromFile.append(content.split())
        content = myFile.readline()

print(fromFile, '\n')

for item in fromFile:
    profit = int(item[2]) - int(item[3])
    item.append(str(profit))
    sum_profit += profit if profit > 0 else 0
    n += 1 if profit > 0 else 0
    firmDict[item[0]] = profit

average_profit = round(sum_profit / n, 2)
goalArray = [firmDict, {"average_profit": average_profit}]

print(goalArray)

with open("myFile7.json", "w") as goalFile:
    json.dump(goalArray, goalFile, ensure_ascii=False)

from random import randint
randomString = [randint(0, 100) for i in range(randint(1, 100))]
randomString = ' '.join(map(str, randomString))

with open("myFile5.txt", "w") as myFile:
    print(randomString, file=myFile)

with open("myFile5.txt") as myFile:
    content = myFile.readline()

intArray = list(map(int, content.split()))
print('Список чисел из файла: {}'.format(intArray))
print('Сумма чисел равна {}'.format(sum(intArray)))

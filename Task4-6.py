from itertools import count, cycle, islice

startNumber = 14
counter = 10

print('a) Первые {} чисел, начиная с {}:'.format(counter, startNumber))
for i in islice(count(startNumber), counter):
    print(i)

array = [1, 4, 12, 3]
counter = 15
print('б) Итерация {} элементов списка {}: '.format(counter, array))
for i in islice(cycle(array), counter):
    print(i)

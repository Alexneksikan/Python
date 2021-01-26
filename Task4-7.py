def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
        yield res


number = int(input('Введите число для вычисления его факториала: '))
if number == 0:
    number = 1  # Факториал нуля равен единице
for el in fact(number):
    print(el)

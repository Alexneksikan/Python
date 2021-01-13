if __name__ == '__main__':

    number = 0
    while number < 1 or number > 9:
        number = int(input('Введите число от 1 до 9: '))

    operand1 = number * 11
    operand2 = number * 111
    summa = number + operand1 + operand2

    print('{} + {} + {} = {}'.format(number, operand1, operand2, summa))

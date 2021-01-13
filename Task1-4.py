if __name__ == '__main__':

    number = '0'
    maxDigit = '0'

    while int(number) < 1:
        number = input('Введите целое положительное число: ')

    digits = list(number)
    length = len(digits)

    i = 1
    while i < length:
        if maxDigit < digits[i]:
            maxDigit = digits[i]
        i += 1

    print('В числе {} самая большая цифра - {}'.format(number, maxDigit))

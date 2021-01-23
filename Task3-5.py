if __name__ == '__main__':

    def my_sum(my_string):
        '''Принимает строку, состояющую из чисел, разделенных пробелами, и возвращает сумму этих чисел'''

        my_string = my_string.strip()
        if len(my_string) != 0:
            return sum([int(item) for item in my_string.split(' ')])
        else:
            return 0


    keyOut = False
    sumNumbers = 0

    while not keyOut:
        inputString = input('Введите несколько чисел через пробел и нажмите Enter. (Для завершения введите букву q): ')
        if inputString.find('q') != -1:
            keyOut = True
            inputString = inputString.replace('q', '')
        sumNumbers += my_sum(inputString)
        print('Сумма равна {}.'.format(sumNumbers))

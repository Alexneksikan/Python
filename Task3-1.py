if __name__ == '__main__':

    def division(number1, number2):
        '''Возвращает частное от деления

        number1 - делимое
        number2 - делитель
        '''

        return number1 / number2


    num1 = int(input('Введите делимое: '))
    num2 = int(input('Введите делитель: '))
    if num2 == 0:
        while num2 == 0:
            num2 = int(input('Делитель не должен быть равен нулю! Повторите ввод: '))

    print('{} / {} = {:.2f}'.format(num1, num2, division(num1, num2)))

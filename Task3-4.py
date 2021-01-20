if __name__ == '__main__':

    def my_func1(x, y):
        '''Принимает числа х и у и возвращает результат возведения числа х в степень у
        Вариант 1
        '''

        return x**y


    def my_func2(x, y):
        '''Принимает числа х и у и возвращает результат возведения числа х в степень у
        Вариант 2
        '''

        i = 0
        result = 1

        while i < abs(y):
            result = result / x
            i += 1

        return result


    number1 = int(input('Введите действительное положительное число Х: '))
    number2 = int(input('Введите целое отрицательное число Y: '))

    print('1 вариант: {} в степени {} равно {:.10f}'.format(number1, number2, my_func1(number1, number2)))
    print('2 вариант: {} в степени {} равно {:.10f}'.format(number1, number2, my_func2(number1, number2)))
    print('Проверка:          pow({}, {}) = {:.10f}'.format(number1, number2, pow(number1, number2)))

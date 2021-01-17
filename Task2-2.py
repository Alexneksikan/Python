if __name__ == '__main__':

    nElements = int(input('Введите количество элементов списка: '))
    i = 0
    array = []
    array1 = []

    while i < nElements:
        array.append(input('Введите {} элемент списка: '.format(i)))
        i += 1

    print('Начальный список: ', array)

    i = 1
    while i < nElements:
        varElement = array[i]
        array.pop(i)
        array.insert(i - 1, varElement)
        i += 2

    print('Итоговый список:  ', array)

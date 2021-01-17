if __name__ == '__main__':

    array = [12, 3.14, 'слово', ('один', 2, 'three'), None, False, 2021]
    i = 0

    for element in array:
        i += 1
        print('{}. {} - тип элемента {}'.format(i, element, type(element)))

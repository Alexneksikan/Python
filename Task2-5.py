if __name__ == '__main__':

    numbers = [8, 6, 6, 5, 5, 4, 3, 3]
    rating = int(input('Введите новый элемент рейтинга (любое целое число): '))
    i = 0
    position = None

    print('ДО:    ', numbers)

    for i in numbers:
        if rating > i:
            position = numbers.index(i)
            numbers.insert(position, rating)
            break

    if position is None:
        numbers.append(rating)

    print('ПОСЛЕ: ', numbers)

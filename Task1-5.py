if __name__ == '__main__':
    revenue = int(input('Выручка фирмы (руб.): '))
    loss = int(input('Издержки фирмы (руб.): '))

    profit = revenue - loss
    if profit >= 0:
        profitMargin = profit / revenue
        print('Фирма работает с прибылью {} руб.'.format(profit))
        print('Рентабельность выручки: {:.2%}'.format(profitMargin))
        staff = int(input('Количество сотрудников (чел.): '))
        profitStaff = profit / staff
        print('Прибыль в расчете на одного сотрудника: {:.2f} руб.'.format(profitStaff))
    else:
        print('Фирма работает с убытком {} руб.'.format(abs(profit)))

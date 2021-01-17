if __name__ == '__main__':

    products = []
    dictProd = {}
    listTuple = ()
    goalDict = {}
    valueList = ['собака', 'кот', 'был']
    i = 1

    while True:
        name = input('Введите название товара (для выхода введите 111): ')
        if name == '111':
            break
        else:
            price = int(input('Введите цену товара: '))
            quantity = int(input('Введите количество товара: '))
            unit = input('Единица измерения: ')
        dictProd = {'Название': name, 'Цена': price, 'Количество': quantity, 'Ед': unit}
        listTuple = (i, dictProd)
        products.append(listTuple)
        i += 1

    print('Товары:')
    for product in products:
        print(product)

    for key in dictProd.keys():
        itemsList = []
        for itemValue in products:
            itemsList.append(itemValue[1][key])
        goalDict[key] = list(set(itemsList))

    print('Итоговый словарь:')
    print('В одну строку: ', goalDict)
    print('Построчно:')
    for k, v in goalDict.items():
        print(k, v)

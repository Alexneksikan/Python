if __name__ == '__main__':

    def printPerson(name, lastName, birthYear, city, email, phone):
        '''Принимает данные клиента и выводит их одной строкой'''

        print('{} {} родился в {} году, живет в городе {}. Электронная почта: {}. Номер телефона: {}.'.format(name, lastName, birthYear, city, email, phone))


    printPerson(name='Александр', lastName='Яковлев', birthYear=1971, city='Магадан', email='alexneksikan@rambler.ru', phone='+7 925-480-76-47')
if __name__ == '__main__':

    def int_func(myword):
        '''Принимает слово из маленьких букв и возвращает это слово с первой заглавной буквой'''

        return myword.title()


    myText = input('Введите текст из строчных латинских букв: ')

    newText = (' '.join([int_func(item) for item in myText.split(' ')]))
    print(newText)

    print(int_func(myText))

if __name__ == '__main__':

    sentence = input('Введите предложение: ')

    arrSentence = sentence.split(' ')
    i = 1

    for word in arrSentence:
        if len(word) > 10:
            word = word[:10]
        print(i, word)
        i += 1

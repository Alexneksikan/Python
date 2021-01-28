with open("myFile2.txt") as myFile:
    counter = 0
    content = myFile.readline()
    while content:
        counter += 1
        print('Строка {:>2} - {:>2} слов: {}'.format(counter, len(content.split()), content[:-2]))
        content = myFile.readline()
print('Всего {} строк'.format(counter))
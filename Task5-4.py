myDict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("myFile4_Eng.txt") as myFile, open("myFile4_Rus.txt", "w") as myFileRus:
    content = myFile.readline()
    while content:
        oneString = content.split()
        oneString[0] = myDict.get(oneString[0])
        print(' '.join(oneString), file=myFileRus)
        content = myFile.readline()

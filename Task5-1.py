with open("myFile1.txt", "w") as myFile:
    zeroString = False
    while not zeroString:
        inString = input('Введите строку и нажмите <Enter>: ')
        if len(inString) != 0:
            print(inString, file=myFile)
        else:
            zeroString = True

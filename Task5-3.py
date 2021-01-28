with open("myFile3.txt") as myFile:
    counter = 0
    sumSalary = 0
    content = myFile.readline()
    print('Сотрудники с доходом менее 20 тыс.:')
    while content:
        fam, salary = content.split()
        salary = int(salary)
        counter += 1
        sumSalary += salary
        if salary < 20000:
            print('{} - {}'.format(fam, salary))
        content = myFile.readline()
print('Средняя величина дохода: {:.2f}'.format(sumSalary / counter))

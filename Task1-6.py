if __name__ == '__main__':

    distanceStart = int(input('Результат в первый день (км): '))
    distanceEnd = int(input('Расстояние для достижения цели (км): '))
    days = 1
    distance = distanceStart

    while distance <= distanceEnd:
        distance = distance * 1.1
        days +=1

    print('На {}-й день спортсмен достиг результата: с {} км до {} км'.format(days, distanceStart, distanceEnd))


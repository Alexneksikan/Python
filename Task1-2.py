if __name__ == '__main__':

    seconds = int(input('Введите время в секундах: '))

    rest = 0
    secs = 0

    hours = seconds // 3600
    if hours > 0:
        rest = seconds % 3600
    else:
        rest = seconds
    minutes = rest // 60
    if minutes > 0:
        secs = rest % 60
    else:
        secs = rest

    print('{} секунд - это {}:{}:{}'.format(seconds, hours, minutes, secs))

class StringError(Exception):
    def __init__(self, txt):
        self.txt = txt


number_string = []
while True:
    item = input("Введите число (для завершения ввода наберите слово stop): ")

    try:
        if item == "stop":
            break
        if not item.isdigit():
            raise StringError("Вы ввели не число! Повторите ввод.")
    except StringError as err:
        print(err)
    else:
        number_string.append(int(item))

print(number_string)

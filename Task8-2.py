class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


in_number1 = input("Введите делимое: ")
try:
    in_number1 = int(in_number1)
except ValueError:
    print("Вы ввели не число")
else:
    in_number2 = input("Введите делитель: ")
    try:
        in_number2 = int(in_number2)
        if in_number2 == 0:
            raise ZeroError("На ноль делить нельзя!!!")
    except ValueError:
        print("Вы ввели не число")
    except ZeroError as err:
        print(err)
    else:
        result = in_number1 / in_number2
        print("{} / {} = {:.2f}".format(in_number1, in_number2, result))

class Complex:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)

    def __str__(self):
        return str(self.x) + " + i" + str(self.y)


print("Введите через пробел действительную и мнимую часть двух комплексных чисел:")
my_x1, my_y1 = input("Первое число: ").split()
my_x1 = int(my_x1)
my_y1 = int(my_y1)
my_x2, my_y2 = input("Второе число: ") .split()
my_x2 = int(my_x2)
my_y2 = int(my_y2)

number1 = Complex(my_x1, my_y1)
number2 = Complex(my_x2, my_y2)
number3 = number1 + number2
number4 = number1 * number2
print("Ответ:")
print("Сложение:  ", number3)
print("Умножение: ", number4)

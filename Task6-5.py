class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Синяя", self.title)


class Pencil(Stationery):
    def draw(self):
        print("Это", self.title)


class Handle(Stationery):
    def draw(self):
        print(self.title, "лежит на столе")


p = Pen("Ручка")
p.draw()

pc = Pencil("Карандаш")
pc.draw()

h = Handle("Маркер")
h.draw()

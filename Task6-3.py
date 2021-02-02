class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p1 = Position("Степан", "Разин", "программист", 10000, 5000)
print(p1.get_full_name())
print(p1.get_total_income())

p2 = Position("Гордон", "Фримен", "учёный", 150000, 150000)
print(p2.get_full_name())
print(p2.get_total_income())
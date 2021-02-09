from random import randint

class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells >= other.cells:
            return Cell(self.cells - other.cells)
        else:
            print("Разность количества ячеек меньше нуля!")
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_in_row):
        cell_string = ""
        x = self.cells // cells_in_row
        y = self.cells % cells_in_row
        for i in range(x):
            cell_string += "\n" + "*" * cells_in_row
        cell_string += "\n" + "*" * y
        print(cell_string)


rows = 5  # количество ячеек в ряду

cell_1 = Cell(randint(5, 20))
cell_2 = Cell(randint(1, 15))
cell_1.make_order(rows)
cell_2.make_order(rows)

print("\nСложение:")
cell_3 = cell_1 + cell_2
cell_3.make_order(rows)
print("\nВычитание:")
cell_4 = cell_1 - cell_2
cell_4.make_order(rows)
print("\nУмножение:")
cell_5 = cell_1 * cell_2
cell_5.make_order(rows)
print("\nДеление:")
cell_6 = cell_1 / cell_2
cell_6.make_order(rows)

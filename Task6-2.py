class Road:

    def weight(self, _length, _width):

        return _length * _width * 25 * 5 / 1000

road_length = int(input("Введите ширину дороги, м: "))
road_width = int(input("Введите длину дороги, м: "))

r = Road()
print("Требуется масса асфальта {:.2f} тонн".format(r.weight(road_length, road_width)))

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if str(self.__class__)[17:-2] == "TownCar":
            print("{} {} - городской автомобиль".format(self.color, self.name))
        if str(self.__class__)[17:-2] == "SportCar":
            print("{} {} - спортивный автомобиль".format(self.color, self.name))
        if str(self.__class__)[17:-2] == "WorkCar":
            print("{} {} - грузовой автомобиль".format(self.color, self.name))
        if str(self.__class__)[17:-2] == "PoliceCar":
            self.is_police = True
            print("{} {} - полицейская машина".format(self.color, self.name))


    def go(self):
        print("{} {} начал движение".format(self.color, self.name))

    def stop(self):
        print("{} {} остановился".format(self.color, self.name))

    def turn(self, direction):
        self.direction = direction
        print("{} {} повернул {}".format(self.color, self.name, self.direction))

    def show_speed(self):
        print("{} {}: скорость: {}".format(self.color, self.name, self.speed))
        str(self.__class__)
        if str(self.__class__)[17:-2] == "TownCar" and self.speed > 60:
            print("ВНИМАНИЕ! Превышение скорости!")
        if str(self.__class__)[17:-2] == "WorkCar" and self.speed > 40:
            print("ВНИМАНИЕ! Превышение скорости!")


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    pass


car1 = TownCar(90, "Белый", "Opel")
car1.go()
car1.show_speed()
car1.turn("направо")
car1.turn("налево")
car1.stop()
print("")

car2 = SportCar(200, "Красный", "Ferrari")
car2.show_speed()
print("is_police =", car2.is_police)
print("")

car3 = PoliceCar(150, "Синий", "Ford")
print("is_police =", car3.is_police)
print("")

car4 = WorkCar(75, "Оранжевый", "МАЗ")
car4.show_speed()

car4 = WorkCar(35, "Оранжевый", "МАЗ")
car4.show_speed()

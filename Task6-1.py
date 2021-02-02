from time import sleep

class TrafficLight:

    def running(self):
        __my_color = "Красный"

        while True:
            print(__my_color)
            if __my_color == "Красный":
                sleep(7)
                __my_color = "Жёлтый"
            elif __my_color == "Жёлтый":
                sleep(2)
                __my_color = "Зелёный"
            else:
                sleep(10)
                __my_color = "Красный"


l = TrafficLight()
l.running()

from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def fabric(self):
        pass


class Coat(Wear):
    def __init__(self, size, counter):
        self.size = size
        self.counter = counter

    @property
    def fabric(self):
        return (self.size / 6.5 + 0.5) * self.counter


class Suit(Wear):
    def __init__(self, height, counter):
        self.height = height
        self.counter = counter

    @property
    def fabric(self):
        return (2 * self.height + 0.3) * self.counter


coat_size, coat_counter = input("Введите через пробел размер пальто и количество: ").split()

coat_size = int(coat_size)
coat_counter = int(coat_counter)

raincoat = Coat(coat_size, coat_counter)
print("{} пальто {} размера: {:.2f} метра ткани".format(coat_counter, coat_size, raincoat.fabric))

input_suit = input("Введите через пробел рост костюма и количество: ")
suit_size, suit_counter = input_suit.split()
suit_size = int(suit_size)
suit_counter = int(suit_counter)

costume = Suit(suit_size, suit_counter)
print("{} костюмов {} размера: {:.2f} метра ткани".format(suit_counter, suit_size, costume.fabric))

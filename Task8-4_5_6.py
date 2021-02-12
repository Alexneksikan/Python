class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    db_storage = {}

    def __init__(self):
        pass

    def __str__(self):
        prn_string = "\nСостояние склада:\n"
        for i_key, i_value in self.db_storage.items():
            prn_string += i_key + " - " + str(i_value) + " шт.\n"
        return prn_string


class OfficeEquipment:
    def __init__(self, name, new=0):
        self.name = name  # название модели
        self.new = new  # новое оборудование или б/у - boolean

    def to_storage(self, equip_count, storage):
        self.equip_count = equip_count
        if self.name in storage.db_storage:
            type_count = storage.db_storage[self.name]
            type_count += equip_count
            del storage.db_storage[self.name]
        else:
            type_count = equip_count
        storage.db_storage[self.name] = type_count
        print("{} в количестве {} шт. приняты на склад.".format(self.name, equip_count))

    def from_storage(self, equip_count, storage):
        self.equip_count = equip_count
        if self.name in storage.db_storage:
            type_count = storage.db_storage[self.name]
            if type_count < equip_count:
                print("Столько нет на складе!")
            else:
                type_count -= equip_count
                del storage.db_storage[self.name]
                storage.db_storage[self.name] = type_count
                print("{} в количестве {} шт. выданы.".format(self.name, equip_count))
        else:
            print("Такого оборудования на складе нет!")


class Printer(OfficeEquipment):

    def __init__(self, name, new=0, equip_type=""):
        super().__init__(name, new)
        self.equip_type = equip_type


class Computer(OfficeEquipment):

    def __init__(self, name, new=0, processor="", memory=0, hdd=0):
        super().__init__(name, new)
        self.processor = processor
        self.memory = memory
        self.hdd = hdd


class Tablet(OfficeEquipment):

    def __init__(self, name, new=0, diagonal=0, os=""):
        super().__init__(name, new)
        self.diagonal = diagonal
        self.os = os


warehouse = Storage()

printer1 = Printer("HP", 1, "laser")
printer2 = Printer("Canon", 0, "inkjet")
comp1 = Computer("MSI", 0, "Intel", 8, 1)
comp2 = Computer("ASUS", 0, "AMD", 16, 2)
tablet1 = Tablet("Samsung", 1, 12, "Win10")
tablet2 = Tablet("Apple", 0, 11, "iOS")

""" Первоначальное заволнение склада """
printer1.to_storage(10, warehouse)
printer2.to_storage(22, warehouse)
comp1.to_storage(25, warehouse)
comp2.to_storage(120, warehouse)
tablet1.to_storage(310, warehouse)
tablet2.to_storage(75, warehouse)

in_out = None
choice_equip = None
new = None
quantity = None
name = None
equip_type = None

while True:
    print(warehouse)
    try:
        in_out = int(input("1 - сдать на склад, 2 - взять со склада, 3 - выход: "))
        if in_out not in range(1, 4):
            raise OwnError("Введите 1, 2 или 3!")
    except ValueError:
        print("Вы ввели не число!")
    except OwnError as err:
        print(err)

    if in_out == 3:
        break

    if in_out == 1:
        try:
            choice_equip = int(input("1 - принтеры, 2 - компьютеры, 3 - планшеты: "))
            if choice_equip not in range(1, 4):
                raise OwnError("Введите 1, 2 или 3!")
        except ValueError:
            print("Вы ввели не число!")
        except OwnError as err:
            print(err)

        if choice_equip == 1:
            try:
                name, new, equip_type, quantity = input("Введите данные через пробел: модель, новый (0) или б/у (1), "
                                                        "тип (laser/inkjet), количество: ").split()
                if not new.isdigit():
                    raise OwnError("Новый или б/у: должно быть 0 или 1!")
                elif int(new) not in (0, 1):
                    raise OwnError("Новый или б/у: должно быть 0 или 1!")
                if not quantity.isdigit():
                    raise OwnError("Количество должно быть числом!")
            except ValueError:
                print("Данные введены в неправильном формате!")
            except TypeError:
                print("Данные введены в неправильном формате!")
            except OwnError as err:
                print(err)
            else:
                new = int(new)
                quantity = int(quantity)
                in_equip = Printer(name, new, equip_type)
                in_equip.to_storage(quantity, warehouse)

        elif choice_equip == 2:
            try:
                name, new, processor, memory, hdd, quantity = input("Введите данные через пробел: модель, новый (0) "
                                                                    "или б/у (1), процессор, размер опер. памяти, "
                                                                    "ёмкость HDD, количество: ").split()
                if not new.isdigit():
                    raise OwnError("Новый или б/у: должно быть 0 или 1!")
                elif int(new) not in (0, 1):
                    raise OwnError("Новый или б/у: должно быть 0 или 1!")
                if not memory.isdigit():
                    raise OwnError("Размер памяти должен быть числом!")
                if not hdd.isdigit():
                    raise OwnError("Объём HDD должен быть числом!")
                if not quantity.isdigit():
                    raise OwnError("Количество должно быть числом!")
            except ValueError:
                print("Данные введены в неправильном формате!")
            except TypeError:
                print("Данные введены в неправильном формате!")
            except OwnError as err:
                print(err)
            else:
                new = int(new)
                memory = int(memory)
                hdd = int(hdd)
                quantity = int(quantity)
                in_equip = Computer(name, new, processor, memory, hdd)
                in_equip.to_storage(quantity, warehouse)

        elif choice_equip == 3:
            try:
                name, new, diagonal, os, quantity = input("Введите данные через пробел: модель, новый (0) или б/у (1), "
                                                          "размер диагонали, операционная система, количество: ").split()
                if not new.isdigit():
                    raise OwnError("Новый или б/у: должно быть 0 или 1!")
                elif int(new) not in (0, 1):
                    raise OwnError("Новый или б/у: должно быть 0 или 1!")
                if not diagonal.isdigit():
                    raise OwnError("Диагональ: должно быть числом!")
                if not quantity.isdigit():
                    raise OwnError("Количество должно быть числом!")
            except ValueError:
                print("Данные введены в неправильном формате!")
            except TypeError:
                print("Данные введены в неправильном формате!")
            except OwnError as err:
                print(err)
            else:
                new = int(new)
                quantity = int(quantity)
                in_equip = Tablet(name, new, diagonal, os)
                in_equip.to_storage(quantity, warehouse)

    if in_out == 2:
        try:
            choice_equip = int(input("1 - принтеры, 2 - компьютеры, 3 - планшеты: "))
            if choice_equip not in range(1, 4):
                raise OwnError("Введите 1, 2 или 3!")
        except ValueError:
            print("Вы ввели не число!")
        except OwnError as err:
            print(err)

        try:
            name, quantity = input("Введите через пробел модель и количество: ").split()
            if not quantity.isdigit():
                raise OwnError("Количество должно быть числом!")
        except ValueError:
            print("Данные введены в неправильном формате!")
        except TypeError:
            print("Данные введены в неправильном формате!")
        except OwnError as err:
            print(err)
        else:
            quantity = int(quantity)
            if choice_equip == 1:
                out_equip = Printer(name)
            elif choice_equip == 2:
                out_equip = Computer(name)
            else:
                out_equip = Tablet(name)
            out_equip.from_storage(quantity, warehouse)

print(warehouse)

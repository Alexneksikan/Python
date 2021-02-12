class Date:
    months = (31, 29, 31, 30, 31, 30, 30, 31, 30, 31, 30, 31)
    date_in = None

    def __init__(self, date_in):
        Date.date_in = date_in

    @classmethod
    def to_number(cls):
        day = int(cls.date_in[0:2])
        month = int(cls.date_in[3:5])
        year = int(cls.date_in[6:])
        return day, month, year

    @staticmethod
    def validation():
        my_day, my_month, my_year = Date.to_number()
        if my_month in range(1, 13):
            if not (my_day in range(1, Date.months[my_month - 1] + 1)):
                print("В {} месяце не может быть {} дн.!".format(my_month, my_day))
            else:
                print("Дата корректная")
        else:
            print("Номер месяца должен быть в диапазоне от 1 до 12!")


dates = ("31-17-1971", "30-02-1991", "05-07-1985")

for d in dates:
    date_1 = Date(d)
    d, m, y = date_1.to_number()
    print("День: {} \nМесяц: {} \nГод: {} ".format(d, m, y))
    Date.validation()
    print("")

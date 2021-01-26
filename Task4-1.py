from sys import argv
script_name, hours, rate, bonus = argv


def salary(nhours, nrate, nbonus):
    return nhours * nrate + nbonus


hours, rate, bonus = [int(i) for i in [hours, rate, bonus]]
print('Заработная плата составляет {:.2f} руб.'.format(salary(hours, rate, bonus)))

from functools import reduce


def multiplier(el_prev, el):
    return el_prev * el


array = [el for el in range(100, 1001) if el % 2 == 0]
multi = reduce(multiplier, array)

print(array)
print(multi)

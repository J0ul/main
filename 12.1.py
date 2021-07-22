# Напишите функцию, которая возвращает разность между наибольшим и наименьшим
# значениями из списка целых случайных чисел.
import random


def diff_min_max(a):
    s = []
    for i in range(a):
        s.append(random.randint(0, 100))
    print(s)
    print(max(s) - min(s))


diff_min_max(3)

# Создайте матрицу (список из вложенных списков) размера N x M (фиксируются в
# программе), заполненную случайными целыми числами
# Вывести номер строки, содержащей максимальное число одинаковых элементов.

from random import randint
from collections import Counter

N = 5 # столбцы
M = 3 # строки
m = [[randint(1, 9) for h in range(N)] for j in range(M)]
print(*m, sep='\n')
maxs = [Counter(x).most_common(1)[0][1] for x in m]
print(maxs)
print(maxs.index(max(maxs))+1)

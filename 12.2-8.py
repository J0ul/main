# 12.2 Напишите программу, которая для целочисленного списка из 1000 случайных
# элементов определяет, сколько отрицательных элементов располагается между его
# максимальным и минимальным элементами.
import random

s = []
for i in range(10):
    s.append(random.randint(-100, 100))

print(s)

a = s.index(min(s))
b = s.index(max(s)) + 1
ss = s[a:b]
print(ss)
count = 0
for i in ss:
    if i < 0 and s.index(i) < b:
        count += 1
print(count)
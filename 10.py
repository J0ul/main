import random

# Найдите все значения функции  y (x) = x**2+ 3
# на интервале от 10 до 30 с шагом 2.
from random import randint

A = list(range(10, 31, 2))
y = list()
for i in A:
    y.append(i ** 2 + 3)
print(y)

# Определить сумму чисел, входящих в список L.
L = [-8, 8, 6.0, 5, 'строка', -3.1]
s = list()
for i in L:
    if type(i) == int:
        s.append(i)
    elif type(i) == float:
        s.append(i)
print(sum(s))

# Дан список числовых значений, насчитывающий N элементов.
# Поменяйте местами первую и вторую половины списка.
Aa = [1, 2, 3, 4, 5, 6]
N = len(Aa)
half_list = int(N/2)
print(half_list)
Bb = list()
for i in Aa[half_list:]:
    Bb.append(i)
for i in Aa[:half_list]:
    Bb.append(i)
Aa = Bb
print(Aa)

#Компьютер загадывает случайное число, пользователь пытается его угадать.
# Пользователь вводит число до тех пор, пока не угадает или не введет слово «Выход».
# Компьютер  сравнивает  число  с  введенным  и  сообщает  пользователю больше оно или меньше загаданного.

X = randint(0, 00)
while True:
    text = int(input("Введите число от 0 до 100 или стоп для выхода: "))
    if text == "стоп":
        print("Выход из программы! До встречи!")
        break
    elif text == X:
        print("Догада!")
        break
    elif text > X:
        print("Меньше!")
    elif text < X:
        print("Больше!")

#Дано число, введенное с клавиатуры. Определите сумму квадратов нечетных цифр в числе.
dig = input("Введите число: ")
sq = 0
for i in range(len(dig)):
    if dig[i] % 2 == 0:
        continue
    sq = sq + i**2
print("сумма квадратов нечетных цифр:", sq)


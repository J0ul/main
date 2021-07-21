
# Дано число, введенное с клавиатуры. Определите сумму квадратов нечетных цифр в числе.
a = input("Введите число: ")
A = list(a)
sq = int(0)
for i in A:
    if int(i) % 2 == 0:
        continue
    else:
        sq = sq + int(i)**2
print(sq)
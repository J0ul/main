dig = input("Введите число: ")
print(dig)
sq = 0
print(dig[0])
D = (list(dig))
print(dig)
for z in list(dig):
    if z % 2 == 0:
        continue
    sq = sq + z**2
print("сумма квадратов нечетных цифр:", sq)

# Дан произвольный текст. Найдите номер первого самого длинного слова в нем.
# Напечатайте все имеющиеся в нем цифры, определите их
# количество, сумму и найти максимальное.
s = "У лукоморья 123 дуб зеленый 456"
l = s.split()
a = list()
d = ""
for i in l:
    if i.isalpha() is True:
        a.append(i)
    else:
        d = d + str.join("", i)

max_word = max(a, key=len)
print(max_word, l.index(max_word) + 1)

print(d)
dd = list(d)
print(len(dd))
for i, item in enumerate(dd):
    dd[i] = int(item)
print(sum(dd))

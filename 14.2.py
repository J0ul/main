# 14.2
# Найдите в файле : http://dfedorov.spb.ru/python/files/mbox-short.txt строки, содержащие
# почтовые адреса. Запишите найденные строки в файл с именем mail.txt.
import urllib.request
import re
mail = []
url = "http://dfedorov.spb.ru/python/files/mbox-short.txt"
with urllib.request.urlopen(url) as webpage:
    for line in webpage:#
        line = line.decode('utf-8')
        result = re.findall(r"[a-zA-Z_0-9.]+@[a-zA-Z_0-9.]+", line)
        for i in result:
            if len(i) > 5 and i not in mail:
                mail.append(i)
with open("mail.txt", "w") as out_file:
    for i in mail:
        i = i + "\n"
        out_file.write(i)

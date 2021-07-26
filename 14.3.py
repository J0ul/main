# 14.3
# Очистите файл от HTML-тегов: http://dfedorov.spb.ru/python/files/p.html
# Выведите на экран «чистый» текст. PS. можно использовать только стандартные модули Python.
import urllib.request
import re
url = "http://dfedorov.spb.ru/python/files/p.html"
text = urllib.request.urlopen(url).read().decode("utf-8")
clear_text = re.sub("<.*?>", "", text)
print(clear_text)

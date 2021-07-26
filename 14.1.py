# 14.1
# Отсортированное по алфавиту содержимое файла plan.txt поместите в файл
# sort_plan.txt.
with open("plan.txt", "r") as file:
    lines = sorted(file.readlines())
with open("sorted_plan.txt", "w") as out_file:
    for i in lines:
        out_file.write(i)

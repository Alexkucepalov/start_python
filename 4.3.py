"""Дан список заполненный произвольными целыми числами.
Получите новый список, элементами которого будут только уникальные элементы исходного.
Примечание. Списки создайте вручную, например так:
my_list_1 = [2, 2, 5, 12, 8, 2, 12]

В этом случае ответ будет:
[5, 8]"""

my_list_1 = [1, 2, 5, 6, 8, 4, 1, 8]
result: list[int] = []
for i in my_list_1:
    if my_list_1.count(i) == 1:
        result.append(i)
print(result)
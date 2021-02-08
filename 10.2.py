"""Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент. Если
список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле. Примечание: Список для проверки
введите вручную. Или возьмите этот: [1, 2, 3, 4] """

import random


def list_random(element):
    if element:
        result = random.choice(element)
        return result
    else:
        return None


print(list_random([1, 2, 3, 4]))
print(list_random([]))

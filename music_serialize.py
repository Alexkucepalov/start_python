"""Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
my_favourite_group = {
‘name’: ‘Г.М.О.’,
‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
{‘name’: ‘Шапито’,‘year’: 2014}]}

С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8. """

my_favourite_group = { 'name': 'Аффинаж.', 'tracks': ['Лучше всех', 'Твой главный враг'],
                       'albums': [{'name': 'Ты, который нашел', 'year': 2018}, {'name': 'Комната с личными вещами', 'year': 2018}]}
print(my_favourite_group)
"""Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.
"""

import os


def creature_directory():
    for i in range(1, 10):
        directory_name = f'dir_{i}'
        os.mkdir(directory_name)


def delete_directory():
    for i in range(1, 10):
        directory_name = f'dir_{i}'
        os.rmdir(directory_name)


if __name__ == '__main__':
    creature_directory()
    #delete_directory()

"""В консольный файловый менеджер добавить проверку ввода пользователя для всех функции с параметрами (на уроке
разбирали на примере одной функции). """
import sys

from core import create_file, create_folder, get_list, delete_file, save_info

save_info('Старт')

try:
    command = sys.argv[1]
except ImportError:
    print('Необходимо выбрать команду. Для выбора команды напишите "help" ')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except ImportError:
            print('Отстутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except ImportError:
            print('Необходимо ввести имя папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except ImportError:
            print('Необходимо ввести имя папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except ImportError:
            print('Необходимо ввести название файла и названии копии')
        else:
            create_file(name, new_name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')

    save_info('Конец')

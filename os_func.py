import os, shutil

def create_dir():
    new_dir = input('Введите имя  папки: ')
    if new_dir in os.listdir(path="."):
        print('Папка/файл уже существует!')
    else:
        os.mkdir(new_dir)
    print(os.listdir(path="."))

def del_filedir():
    del_dir = input('Введите имя  папки: ')
    if del_dir not in os.listdir(path="."):
        print('Папка/файл не существует!')
    elif os.path.isdir(del_dir) and len(os.listdir(path=del_dir)) == 0:
        os.rmdir(del_dir)
    else:
        shutil.rmtree(del_dir)

def del_filedir():
    del_dir = input('Введите имя  папки: ')
    if del_dir not in os.listdir(path="."):
        print('Папка/файл не существует!')
    elif os.path.isdir(del_dir) and len(os.listdir(path=del_dir)) == 0:
        os.rmdir(del_dir)
    else:
        shutil.rmtree(del_dir)

def copy_filedir():
    copy_from = input('Введите имя исходной папки/файла: ')
    if  copy_from not in os.listdir(path="."):
        print('Исходный папка/файл не существует!')
    else:
        copy_to = input('Введите имя целевой папки/файла: ')
        if os.path.isfile(copy_from):
            shutil.copyfile(copy_from, copy_to)
        else:
            shutil.copytree(copy_from, copy_to)

def show_curr_dir():
    print('Рабочая директория:')
    for i in os.listdir(path="."):
        print('    ', i)

def show_dir():
    print('Папки в рабочей директорий:')
    for i in os.listdir(path="."):
        if os.path.isdir(i):
            print('    ', i)

def show_file():
    print('Файлы в рабочей директорий:')
    for i in os.listdir(path="."):
        if os.path.isfile(i):
            print('    ', i)

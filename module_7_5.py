# Домашнее задание по теме "Файлы в операционной системе"

import os
import time
from datetime import datetime

current_dir = os.getcwd() # рабочая директория
print(current_dir)

files_in_dir = os.listdir(current_dir) # список файлов из рабочей директории
# for i in files_in_dir: # печать простого перечня названий файлов
#   print(i, end='\n')

for file_name in files_in_dir:  # печать полного пути к файлам из рабочей директории
    if os.path.isfile(file_name): # возвращает True если путь path существует и является обычным файлом
        file_path = os.path.join(current_dir, file_name)
        filetime = os.path.getctime(file_name)
        formatted_time = datetime.fromtimestamp(filetime) # дата из стандартного представления времени
        file_size = os.path.getsize(file_name)
        parent_dir = os.path.dirname(current_dir)
        print(f'Обнаружен файл: {file_name}, Путь: {file_path}, Размер: {file_size} байт, '
                   f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Пример возможного вывода:

# Обнаружен файл: module_7_5.py, Путь: C:\Users\Asus\Downloads\Project_Python_Urban\pythonProject\M7\module_7_5.py,
# Размер: 2376 байт, Время изменения: 2025-01-07 14:00:16.310628,
# Родительская директория: C:\Users\Asus\Downloads\Project_Python_Urban\pythonProject

directory = "."

for files in os.walk(directory): # обход всех директорий
    print(files)

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(root, file)
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname(file)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Пример возможного вывода:

# Обнаружен файл: module_7_5.py, Путь: module_7_5.py, Размер: 1374 байт,
# Время изменения: 07.01.2025 15:09, Родительская директория:





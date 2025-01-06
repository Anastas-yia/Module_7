# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    strings_positions = {}
    index = 1
    file = open(file_name, 'w', encoding='utf8')
    for string in strings:
        position = file.tell()  # Получение номера байта начала строки используем метод tell()
        file.write(string + '\n')
        strings_positions[(index, position)] = string # Формируем словарь ключ : значение
        index += 1
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')
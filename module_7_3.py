# Домашнее задание по теме "Оператор "with"
# Задача "Найдёт везде"
import string

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = [*file_names]

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf8') as file:
                words_list = []
                for line in file:
                    line = line.lower()
                    for p in string.punctuation:
                        if p in line:
                            line = line.replace(p, '')
                    words_list.extend(line.split())
            all_words[file_name] = words_list
        return all_words

    def find(self, word):
        word_position = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                word_position[key] = value.index(word.lower()) + 1
        return word_position

    def count(self, word):
        word_count = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                word_count[key] = value.count(word.lower())
        return word_count

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# Вывод на консоль:

# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки',
#                    'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}

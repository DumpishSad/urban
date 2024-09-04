import re


class WordsFinder:
    def __init__(self, *fileNames):
        self.file_names = fileNames

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                s = "".join([string for string in file])
                all_words[name] = re.split(r"[,.=!?;:\s\-\n]+", s)
        return all_words

    def find(self, word):
        dictionary = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dictionary[name] = words.index(word.lower()) + 1
        return dictionary

    def count(self, word):
        dictionary = {}
        for name, words in self.get_all_words().items():
            dictionary[name] = words.count(word.lower())
        return dictionary


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

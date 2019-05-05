
# 1. Создайте класс Word.
# 2. Добавьте свойства text и part of speech.
# 3. Добавьте возможность создавать объект слово со значениями в скобках.
# 4. Создайте класс Sentence
# 5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
# 6. Добавьте метод show, составляющий предложение.
# 7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.

import pymorphy2
import re

morph = pymorphy2.MorphAnalyzer()


class Word:                      # 1. Создайте класс Word.
    text = None                  # 2. Добавьте свойства text и part of speech.
    part_of_speech = None

    def __init__(self, text, part_of_speech):
        self.text = text
        self.part_of_speech = morph.parse(text)[0]


random_word = Word("Черепашка", 1 )                # 3. Добавьте возможность создавать объект слово со значениями в скобках.
print(random_word.text)                                   # наше слово
print("Часть речи:", random_word.part_of_speech.tag.POS)  # его часть речи. NOUN = существительное

class Sentence:                                    # 4. Создайте класс Sentence
    content = None                                 # 5. Добавьте свойство content...
    def __init__(self, text):
        self.text = text.split()
        self.content = list(range(len(self.text)))  #... равное списку, состоящему из номеров слов, входящих в предложение.

    def show(self):                                 # 6. Добавьте метод show, составляющий предложение.
        for i in range(len(self.text)):
            print(self.text[i], end = ' ')

    def show_parts(self):                          # 7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.
        print("\n","Части речи в тексте:")
        for i in range(len(self.text)):
           return (morph.parse(self.text[i]))


somewords = Sentence("Пельмешка упала на пол, а кот её съел")
print ("Номера слов в предложении:", somewords.content)
sometext = somewords.show()
textsp = somewords.show_parts()
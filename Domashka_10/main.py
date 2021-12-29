#Класс Alphabet

#Создайте класс Alphabet
#Создайте метод init(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
#Создайте метод print(), который выведет в консоль буквы алфавита
#Создайте метод letters_num(), который вернет количество букв в алфавите
#Класс EngAlphabet

#Создайте класс EngAlphabet путем наследования от класса Alphabet
#Создайте метод init(), внутри которого будет вызываться родительский метод init().
# В качестве параметров ему будут передаваться обозначение языка(например, ‘En’) и строка,
# состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
#Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
#Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта буква к английскому алфавиту.
#Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
#Создайте статический метод example(), который будет возвращать пример текста на английском языке.
#Задания:

#Создайте объект класса EngAlphabet
#Напечатайте буквы алфавита для этого объекта
#Выведите количество букв в алфавите
#Проверьте, относится ли буква F к английскому алфавиту
#Проверьте, относится ли буква Щ к английскому алфавиту
#Выведите пример текста на английском языке
#Сделайте тоже для русского алфавита
import string
#import engAlphabet
class Alphabet:
    def __init__(self, lang, letters: list):
        self.__lang = lang
        self.__letters = letters

    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self,value):
        self.__lang = value

    @property
    def letters(self):
        return self.__letters

    @letters.setter
    def letters(self, value):
        self.__letters = value

    def print(self):
        for letter in self.__letters:
            print(letter)

    def __repr__(self):  #выведет в консоль буквы алфавита
        return f'{self.__letters}'

    # Создайте метод letters_num(), который вернет количество букв в алфавите
    def letters_num(self): #вернет количество букв в алфавите
        return f'Количество букв в английском алфавите {len(self.__letters)}'

#Создайте класс EngAlphabet путем наследования от класса Alphabet
#Создайте метод init(), внутри которого будет вызываться родительский метод init().
# В качестве параметров ему будут передаваться обозначение языка(например, ‘En’) и строка,
# состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
class EngAlphabet(Alphabet):

    def __init__(self, lang, letters, lang_disignation, a_u):
        super().__init__(lang, letters)
        self.a_u = a_u
        self.lang_disignation = lang_disignation

    @property
    def a_u(self):
        return self.__a_u

    @a_u.setter
    def a_u(self, value):
        self.__a_u = value


    # Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
    __letters_num = len(string.ascii_uppercase)

    # Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта буква к английскому алфавиту.
    def is_en_letter(self, char_: str):
        if char_ in self.a_u:
            print ('Буква', char_, 'относится к английскому алфавиту')
        else:
            print ('Буква', char_, 'не относится к английскому алфавиту')

    # Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
    def letters_num(self): #будет возвращать значение свойства __letters_num.
        return f'Количество букв в английском алфавите - {len(self.__a_u)}'

    # Создайте статический метод example(), который будет возвращать пример текста на английском языке.
    @staticmethod
    def example():
        print('Walking, running, cycling and playing football are some kinds of sports that you do every day. ' \
               'Some people think that doing sports is useless, the other consider that it is tiring. ' \
               'So, why is it so important to do sports?')



#Создайте объект класса EngAlphabet
#Напечатайте буквы алфавита для этого объекта
#Выведите количество букв в алфавите
#Проверьте, относится ли буква F к английскому алфавиту
#Проверьте, относится ли буква Щ к английскому алфавиту
#Выведите пример текста на английском языке
#Сделайте тоже для русского алфавита

alf1 = EngAlphabet('Inglish', ['H', 'e', 'l', 'l', 'o'],'En', string.ascii_uppercase)
alf1.print()
print(alf1.letters_num())
alf1.is_en_letter('F')
alf1.is_en_letter('Щ')
EngAlphabet.example()  #- почему не могу через returne и как через str

alf2 = EngAlphabet('Russian', ['П', 'р', 'и', 'в', 'е', 'т'],'Ru', string.ascii_uppercase)
alf2.print()


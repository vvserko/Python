#Создайте метод init(), внутри которого будет вызываться родительский метод init().
# В качестве параметров ему будут передаваться обозначение языка(например, ‘En’) и строка,
# состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
class EngAlphabet(Alphabet):
    def __init__(self, lang, letters, lang_disignation, a_u=string.ascii_uppercase):
        super().__init__(lang, letters)

        self.lang_disignation = lang_disignation
        self.a_u = a_u

    # Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
    __letters_num = len(string.ascii_uppercase)

    # Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли эта буква к английскому алфавиту.
    def is_en_letter(self, char):
        if char in self.a_u:
            return f'True'

    # Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
    def letters_num(self): #будет возвращать значение свойства __letters_num.
        return super().len(self.__letters)

    # Создайте статический метод example(), который будет возвращать пример текста на английском языке.
    @staticmethod
    def example():
        return 'Walking, running, cycling and playing football are some kinds of sports that you do every day. ' \
               'Some people think that doing sports is useless, the other consider that it is tiring. ' \
               'So, why is it so important to do sports?'
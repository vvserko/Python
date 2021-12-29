#Описать класс «домашняя библиотека».
#Предусмотреть возможность работы с произвольным числом книг,
#поиска книги по какому-либо признаку (например, по автору или по году издания),
#добавления книг в библиотеку, удаления книг из нее, сортировки книг по разным полям.
import os
import atexit
import pickle
import poisk

class Home_library:
    def __init__(self, name_book, author_book, date_book):
        self.__name_book = name
        self.__author_book = author_book
        self.__date_book = date_book
    @property
    def name_book(self):
        return self.__name_book

    @name_book.setter
    def name_book(self,value):
        self.__name_book = value

    @property
    def author_book(self):
        return self.__author_book

    @author_book.setter
    def author_book(self, value):
        self.__author_book = value

    @property
    def date_book(self):
        return self.__date_book

    @date_book.setter
    def date_book(self, value):
        self.__date_book = value

    def __str__(self):
        return f'{self.__name_book}, {self.__author_book}, {self.__date_book}'

    def __repr__(self):
        return f"{self.__name_book}, {self.__author_book}, {self.__date_book})"

def exit_handler():
    with open('books.txt', 'ab') as file:
        pickle.dump(books, file)

atexit.register(exit_handler)

books = []
while True:
    n = int(input('Для вывода списка книг введите 0\nДля добавления книги введите 1\nДля удаления книги введите 2\n'
                  'Для сортировки книг по автору введите 3\nДля поиска книги введите 4\n'
                  'Для выхода введите 5\n'))
    if n == 1:
        os.system('cls')
        name = input('Введите название книги:')
        author = input('Введите автора:')
        date = input('Введите год издания:')
        book = Home_library(name, author, date)
        books.append(book)

        for book in books:
            print(book)

    elif n == 2:
        os.system('cls')
        for book in books:
            print(book)
        book_del = int(input('Введите номер удаляемой книги:'))
        books[book_del-1] = ''
        for book in books:
            print(book)

    elif n == 3:
        os.system('cls')
        books = sorted(books, key=lambda t: t.author_book)
        for book in books:
            print(book)

    elif n == 4:
        item = str(input('Введите признак поиска ("автор" или "год издания")'))
        if item == 'автор':
            item = input('Введите автора: ')
        else:
            item = input('Введите год издания: ')
        os.system('cls')
        poisk.find_book(books, item)

    elif n == 0:
        for book in books:
            print(book)

    elif n == 5:
        break


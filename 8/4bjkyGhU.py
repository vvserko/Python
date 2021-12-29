import turtle
import math

t = turtle.Turtle()


def square(side):
    for _ in range(4):
        t.forward(side)
        t.left(90)


for n in range(10):
    square(500 - n * 10 * 2)
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()

turtle.mainloop()

##################

#Компьютер загадывает число от 1 до 10. У пользователя 5 попыток отгадать.
# После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число.
# В конце игры текст с результатом (или “Вы угадали”, или “Попытки закончились”).
import random
x = random.randint(1,10)
for n in range(5):
    y = int(input('Please input number '))
    if y > x:
        print('>')
    elif y < x:
        print('<')
    elif y == x:
        print('You win')
        break
    else:
        print('Attempts ', n + 1)
else:
    print('You lose')


######################################


# Дано предложение.
# Заменить группы пробелов одиночными,
# крайние пробелы удалить.
# Все слова перевести в нижний регистр,
# первые буквы сделать заглавными.
# найти все числа и разделить их на 2
my_str = ' Тихий летний       вечер. 123 Солнышко, притомившись светить, 345 отправилось на заслуженный 23 покой до рассвета.'

while '  ' in my_str:
    my_str = my_str.replace('  ', ' ')

my_str = my_str.strip()
my_str = my_str.lower()
my_str = my_str.title()
words = my_str.split(' ')

for word in words:
    if word.isnumeric():
        float = int(word) / 2
        print(float)
        my_str = my_str.replace(word, str(float))

print(my_str)

##############################

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('My first supe puper app')
window.geometry('500x500')

def clicked():
    text = entry.get()
    text = text[::-1]
    messagebox.showerror('hello', text)
    label.configure(text=text)

label = Label(window, text='World')
label.grid(column=0, row=0)

button = Button(window, text='Click me', command=clicked)
button.grid(column=1,row=0)


entry = Entry(window, width=20)
entry.grid(column=0, row=1)

window.mainloop()

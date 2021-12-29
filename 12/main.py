# task - текст, приоритет, статус
import atexit
import pickle
from task import Task
import os
tasks = []
 
def exit_handler():
    with open('tasks.data', 'wb') as file:
        pickle.dump(tasks, file)
 
atexit.register(exit_handler)
 
with open('tasks.data', 'rb') as file:
    try:
        tasks = pickle.load(file)
    except EOFError as error:
        print('В файле нет задач')
 
 
while True:
    n = int(input('Для ввода задачи введите 1\nДля выполнения задачи введите 2\nДля вывода списка введите 3\n'))
 
    if n == 1:
        os.system('cls')
 
        text = input('Текст: ')
        priority = int(input('Приоритет от 1 до 10: '))
        t = Task(text, priority, False)
        tasks.append(t)
 
    if n == 2:
        os.system('cls')
 
        for i, t in enumerate(tasks):
            if not t.status:
                print(i, '|', t)
        task_number = int(input('Введите номер задачи для выполнения'))
        tasks[task_number].status = True
 
    if n == 3:
        os.system('cls')
 
        tasks = sorted(tasks, key=lambda t: t.priority, reverse=True)
        for t in tasks:
            print(t)
 
    if n == 4:
        break
 
 
##########################################################
 
 
from turtle import Turtle, mainloop, onscreenclick
 
bob = Turtle()
bob.speed('fastest')
 
 
def square():
    for _ in range(4):
        bob.forward(100)
        bob.left(90)
 
 
def line():
    for _ in range(3):
        square()
        bob.forward(100)
 
 
def place():
    for _ in range(3):
        line()
        bob.left(180)
        bob.forward(300)
        bob.right(90)
        bob.forward(100)
        bob.right(90)
 
 
def draw_x(x, y):
    bob.penup()
    bob.setposition(x * 100, y * 100)
    bob.pendown()
    bob.setposition(x * 100 + 100, y * 100 + 100)
    bob.penup()
    bob.setposition(x * 100, y * 100 + 100)
    bob.pendown()
    bob.setposition(x * 100 + 100, y * 100)
 
 
def draw_o(x, y):
    bob.penup()
    bob.setposition(x * 100 + 50, y * 100)
    bob.pendown()
    bob.circle(50)
 
 
map = [['', '', ''], ['', '', ''], ['', '', '']]
order = 1
 
 
def fun(x, y):
    x = int(x // 100)
    y = int(y // 100)
    global order
    if order:
        draw_o(x, y)
        map[y][x] = 'o'
    else:
        draw_x(x, y)
        map[y][x] = 'x'
    order = not order
    win_condition()
 
 
place()
onscreenclick(fun)
 
 
def win_condition():
    for l in map:
        if l.count('x') == 3:
            print('x - win')
            break
        if l.count('o') == 3:
            print('o - win')
            break
 
    index = 0
    while index < len(map[0]):
        temp = []
        for l in map:
            temp.append(l[index])
            if temp.count('x') == 3:
                print('x - win')
                break
            if temp.count('o') == 3:
                print('o - win')
                break
        index += 1
 
    index = 0
    temp = []
    while index < len(map[0]):
        temp.append(map[index][index])
        index += 1
 
    if temp.count('x') == 3:
        print('x - win')
    if temp.count('o') == 3:
        print('o - win')
 
    index_x = 0
    index_y = len(map[0]) - 1
    temp = []
    while index_x < len(map[0]):
        temp.append(map[index_y][index_x])
        index_x += 1
        index_y -= 1
 
    if temp.count('x') == 3:
        print('x - win')
    if temp.count('o') == 3:
        print('o - win')
 
 
mainloop()
 
 
 
 
#################################
 
import turtle
 
def triangle(angle):
    bob = turtle.Turtle(visible=False)
    bob.speed('fastest')
    bob.left(angle)
    bob.forward(100)
    bob.left(120)
    bob.forward(100)
    bob.left(120)
    bob.forward(100)
    bob.left(120)
    turtle.resetscreen()
    triangle(angle+2)
 
triangle(0)
 
 
 
turtle.mainloop()

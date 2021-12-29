import turtle
import math

plotter = turtle.Turtle(visible=False)

plotter.speed('fastest')

scale = 80
x_size = int(scale/4)
y_size = int(scale/8)
for x in range(-x_size, x_size+1):
    plotter.setposition(x*scale, 0)
    plotter.dot()

plotter.penup()
plotter.setposition(0, -y_size*scale)
plotter.pendown()
for y in range(-y_size, y_size+1):
    plotter.setposition(0, y*scale)
    plotter.dot()

plotter.penup()


x = -5
while x <= 5:
    plotter.setposition(x*scale, math.cos(x)*scale)
    plotter.pendown()
    x += 0.2



turtle.mainloop()











import string

print(string.punctuation)
with open('books.txt', 'r', encoding='utf8') as file:
    max_len_word =''
    for line in file:
        for punk in string.punctuation:
            if punk == '-':
                continue
            line = line.replace(punk, '')
        words = line.split(' ')
        max = ''
        for word in words:
            if len(word) > len(max):
                max = word
        if len(max) > len(max_len_word):
            max_len_word = max

    print(max_len_word)


import string

print(string.punctuation)
with open('books.txt', 'r', encoding='utf8') as file:
    dict = dict()
    for line in file:
        for punk in string.punctuation:
            if punk == '-':
                continue
            line = line.replace(punk, '')
        words = line.split(' ')
        for word in words:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
    max_lengths = sorted(dict.values(), reverse=True)
    for i in range(100):
        for key, value in dict.items():
            if value == max_lengths[i]:
                print('Word: ', key,' count: ', value)


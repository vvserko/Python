

# Задача 1. Дан файл с логинами и паролями. Найдите топ10 самых популярных паролей.
pwd = open('pwd.txt', 'r', encoding='utf8')

spisok = []

for line in pwd:
    a = pwd.readline()
    element = a.split(';')
    spisok.append(element)

d = dict(spisok)
pwd.close()
#print(d)
paroly = list(d.values()) # список из паролей
#print(paroly)


mn = {}
for parol in paroly:
    count = int(paroly.count(parol))
    mn.update({parol: count})


dict1 = {1: 1, 2: 9, 3: 4}
sorted_dict = {}
sorted_keys = sorted(mn, key=mn.get, reverse=True)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = mn[w]

#print(sorted_dict)

sort_kort = list(sorted_dict.items())

i = 0
while i < 10:
    print(sort_kort[i])
    i += 1



    # Задача 2. Пользователь вводит формулу вида max(a,b) или min(a,b),
# где a,b - целые числа или аналогичные выражения min(), max(). Найти значение выражения. Примеры: max(1,5) = 5,

s = input('Введите:')
s = s[4:-1]
s2 = s[0:3]

if s2 == max:
    s = s.split(',')
    print(s)
    print('Максимальное значение - ', max(s))
else:
    s = s.split(',')
    print(s)
    print('Минимальное значение - ', min(s))


    # Задача 3. Создать программу, переписывающую в текстовый файл g содержимое файла f, исключая пустые строки,
# а остальные дополнить справа пробелами или ограничить до n символов.
f = open('f.txt', 'r')
g = open('g.txt', 'w')

for line in f:
    if line == '\n':
        continue
    s = line + ' '
    g.write(s)


g.close()
f.close()

#--------------------------------------------

f = open('f.txt', 'r', encoding='utf8')
g = open('g.txt', 'w', encoding='utf8')
n = 80

for line in f:


    if line == '\n':
        continue
    else:
        s = ''
        i = 0
        while i <= n and i < len(line):
           s = s + line[i]
           i += 1
        print(s)

    g.write(s)


g.close()
f.close()


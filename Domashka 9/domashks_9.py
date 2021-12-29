
#Задача
#Написать программу TODO List (список задач)

#В задаче должны присутствовать текст, приоритет, статус

#Хранить задачи в файле

#Организовать изменение статуса и добавление задач

#Задачи должны быть отсортированы по приоритету

def new_task():
    task = str(input("Введите задачу "))
    pr = str(input("Введите приоритет (H, L):"))
    st = str(input("Введите статус (""Complete"", ""In work"")"))
    f.write(f"{i}-{task}||Приоритет-{pr}||Статус-{st}"+'\n')


#def corect_status():



# Блок 1 - создание задачи
f = open('todo.txt', 'w')
i = 1
new_task()
f.close()

# Блок 2 - добавление задачи
j = 1
while j != 0:
    j = int(input('Введите "1" для введения задачи или "0" для выхода'))
    if j == 0:
        break
    i += 1
    f = open('todo.txt', 'a')
    new_task()
    f.close()

#Вывод на консоль задач
f = open('todo.txt', 'r')
for line in f:
    s = line
    print(s)
f.close()


# Блок 3 - Изменение статуса задачи

sp = []
f = open('todo.txt', 'r+')
for line in f:
    s = line
    s = s[0:len(s) - 1]
    sp.append(s)

number_str = int(input("Введите номер строки для изменения статуса"))
for el in sp:
    if el[0] == number_str:
        if el.find('Complete') == -1:
            el = el.replace('In work', 'Complete')
        else:
            el = el.replace('Complete', 'In work')

for el in sp:
    f.write(el + '\n')

f.close()


# Блок 4 - сортировка по приоритету
sp = []
f = open('todo.txt', 'r+')
for line in f:
    s = line[0:len(line) - 1]
    sp.append(s.split('||'))
    for el in sp:
        el = el.split('-')


sorted(sp, key=lambda x: sp[2][2])

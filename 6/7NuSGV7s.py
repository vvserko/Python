l = [1, 2, 54, 67, 234, -67, 8, 34, 65, 345, -23, 91]
min = max(l)
for element in l:
    if element < min and element % 2 == 0:
        min = element
print(min)


#----------------------------------------------

#Дана строка. Вывести ее три раза через запятую и показать количество символов в ней.
s = 'abc'
new_s = s
for n in range(799):
    new_s = new_s + ','+ s

print(new_s)

#------------------------------
#Дана строка. Вывести первые три символа и последний три символа, и все четные по индексу символы
#s = s[start:end:step]
s = 'abcabcsadfasdfasdfasddfas'
print(s[:3], s[-3:], s[::2])



#------------------------------------

# Удалить точку из строки
s = 'AdfcvD.fdscvAdfAfvh'
dot_index = s.find('.')
s = s[:dot_index] + s[dot_index+1:]
print(s)

#------------------------------
# Удалить лишние пробелы
s = 'Adf                                                acv    D.    .f.d    ;scvA    dfAfvh'
while '  ' in s:
    s = s.replace('  ', ' ')
print(s)


# ----------------------------

# join and split
s = 'Adf acv D. .f.d ;scvA dfAfvh'

list = s.split(' ')
new_list = []

for element in list:
    if len(element) >= 4:
        new_list.append(element)

new_s = ' '.join(new_list)
print(new_s)



#----------------------------------

#Дана строка. Определите, какой символ в ней встречается раньше: 'x' или 'w'.
# Если какого-то из символов нет, вывести сообщение об этом.
str = 'asdfxsfasdfw'
x = str.find('x')
w = str.find('w')

if x == -1 or w == -1:
    print('net')
elif x < w:
    print('x')
else:
    print('w')

#--------------------------------
#Даны две строки. Вывести большую по длине строку столько раз,
# на сколько символов отличаются строки.
s1 = 'a21434'
s2 = 'asdsdfasdfasd'
length_s1 = len(s1)
length_s2 = len(s2)
multiplayer = abs(length_s1-length_s2)
if length_s1 > length_s2:
    print(s1*multiplayer)
else:
    print(s2*multiplayer)

#-------------------------------

#Дана строка. Если она начинается на 'abc',
# то заменить их на 'www', иначе добавить в конец строки 'zzz'.
str = 'abcasdfasdfasdfas'
if str.startswith('abc'):
    str = str.replace('abc', 'www', 1)
else:
    str = str + 'zzz'
print(str)


#----------------------------------

# Дана строка. Если ее длина больше 10, то оставить в строке только первые 6 символов,
# иначе дополнить строку символами 'o' до длины 12.

str = '12345'
if len(str) > 10:
    str = str[:6]
else:
    str = str + '0'*(12-len(str))
print(str)

#--------------------------------

# Пользователь вводит последовательность цифр, разделенных пробелами.
# Посчитать сумму последовательности
str = input('Пожалуйст введите цифры, разделяя пробелами: ')
print('String ', str)
strings = str.split(' ')
print('Strings ', strings)
sum = 0
for s in strings:
    sum = sum + int(s)
print('Sum', sum)



# Дана предложение. Удалить первую букву в каждом слове
str = 'Если форматируемое число больше то мы можем указать в определении плейсхолдера'

words = str.split(' ')
new_words = []
for word in words:
    new_words.append(word[1:])
new_str = ' '.join(new_words)
print(new_str)



#-----------------------------
# Дана предложение. Удалить первую букву в каждом слове
str = 'Если форматируемое число больше то мы можем указать в определении плейсхолдера'

words = str.split(' ')
new_str = ' '
for word in words:
    new_str = new_str + word[1:] + ' '
new_str = new_str[:-1]
print(new_str)
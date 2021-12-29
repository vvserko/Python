#Класс Phone.
#Создайте класс Phone, который содержит переменные number, model и weight.
#Создайте три экземпляра этого класса.
#Выведите на консоль значения их переменных.
#Добавить в класс Phone методы:
#receiveCall, имеет один параметр – имя звонящего. Выводит на консоль сообщение “Звонит {name}”.
#getNumber – возвращает номер телефона. Вызвать эти методы для каждого из объектов.
#Добавить конструктор в класс Phone, который принимает на вход три параметра для
  # инициализации переменных класса - number, model и weight.
#Создать метод sendMessage с аргументами переменной длины.
 # Данный метод принимает на вход номера телефонов, которым будет отправлено сообщение.
 # Метод выводит на консоль номера этих телефонов.
class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def vyvod_na_cosole(self):
        print(self.number, self.model, self.weight)

    def receiveCall(self, name):
        self.name = name
        print(f'Звонит {self.name}')

    def getNumber(self):
        print(f'Возвращаемый номер телефона {self.number}')

    def sendMessage(self, *number):
        if self.number in number:
            print('Номер телефона:', self.number)



ph1 = Phone('111', 'Sony', 100)
ph2 = Phone('222', 'Sumsung', 95)
ph3 = Phone('333', 'Redmi', 120)
name = str(input('Enter name:'))
ph1.vyvod_na_cosole()
ph2.vyvod_na_cosole()
ph3.vyvod_na_cosole()

ph1.receiveCall(name)

ph1.getNumber()

ph1.sendMessage(ph1.number)


#Задача 2
#Класс Покупатель с полями Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, Номер банковского счета;

#Конструктор;
#Методы:
#установка значений атрибутов,
#получение значений атрибутов,
#вывод информации.
#Создать список объектов данного класса.
#Вывести список покупателей в алфавитном порядке
#Вывести список покупателей, у которых номер кредитной карточки находится в заданном диапазоне.
class Customer:
    def __init__(self, l_name, f_name, otchestvo, adress, c_c_number, b_number):
        self.l_name = l_name
        self.f_name = f_name
        self.otchestvo = otchestvo
        self.adress = adress
        self.c_c_number = c_c_number
        self.b_number = b_number

    @property
    def l_name(self):
        return self.l_name
    @l_name.setter
    def l_name(self):
        return self.l_name

    @property
    def f_name(self):
        return self.f_name
    @f_name.setter
    def f_name(self):
        return self.f_name

    @property
    def otchestvo(self):
        return self.otchestvo
    @otchestvo.setter
    def otchestvo(self):
        return self.otchestvo

    @property
    def adress(self):
        return self.adress
    @adress.setter
    def adress(self):
        return self.adress

    @property
    def c_c_number(self):
        return self.c_c_number
    @c_c_number.setter
    def c_c_number(self):
        return self.c_c_number

    @property
    def b_number(self):
        return self.b_number
    @b_number.setter
    def b_number(self):
        return self.b_number



    def spis(self):
        return []

    def __str__(self):
        return f'{self.l_name}, {self.f_name}, {self.otchestvo}, {self.adress}, {self.c_c_number}, {self.b_number}'

    def mass(self):
        return [self.l_name, self.f_name, self.otchestvo, self.adress, self.c_c_number, self.b_number]

    def get_is_perfect(self):
        diapazon = True
        for r in self.c_c_number:
            if r < 1111 and r > 3333:
                flag = False
                break
        return diapazon




#Создать список объектов данного класса.

customer1 = Customer('la_name1', 'f_name1', 'otchestvo1', 'adress1', 5555, 'b_number1')
customer2 = Customer('lc_name2', 'f_name2', 'otchestvo2', 'adress2', 2222, 'b_number2')
customer3 = Customer('lb_name3', 'f_name3', 'otchestvo3', 'adress3', 8888, 'b_number3')
customers = [customer1, customer2, customer3]

d1 = customer1.mass()
d2 = customer2.mass()
d3 = customer3.mass()
p = [d1, d2, d3]

#print(p)
#Вывести список покупателей в алфавитном порядке

s = []
for el in p:
    s.append(el[0])

print(s)
s = sorted(s, reverse=0)
print(s)
#Вывести список покупателей, у которых номер кредитной карточки находится в заданном диапазоне.

for el in p:
    if el[4] > 1111 and el[4] < 3333:
        print(el[4])

        #Задача 3
#Создайте пример наследования, реализуйте класс Student и класс Aspirant,
# аспирант отличается от студента наличием некой научной работы.

#Класс Student содержит переменные: firstName, lastName, group. А также, averageMark, содержащую среднюю оценку.
#Создать метод getScholarship() для класса Student, который возвращает сумму стипендии.
# Если средняя оценка студента равна 5, то сумма 100 грн, иначе 80.
#Переопределить этот метод в классе Aspirant. Если средняя оценка аспиранта равна 5, то сумма 200 грн, иначе 180.
#Создать список из 10 элементов типа Student и Aspirant. Вызвать метод getScholarship() для каждого элемента массива
class Student:
    def __init__(self, firstName, lastName, group, averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark

    def getScholarship(self):
        if self.averageMark == 5:
            money = 100
        else:
            money = 80
        return money




class Aspirant(Student):
    def getScholarship(self):
        if self.averageMark == 5:
            money = 200
        else:
            money = 180
        return money

st1 = Student('f_name1', 'la_name1', 'gr1', 5)
st2 = Student('f_name2', 'la_name2', 'gr2', 4)
st3 = Student('f_name3', 'la_name3', 'gr3', 3)
students = [st1, st2, st3]
for el in students:

    print(el.getScholarship())

st1 = Aspirant('f_name1', 'la_name1', 'gr1', 5)
st2 = Aspirant('f_name2', 'la_name2', 'gr2', 4)
st3 = Aspirant('f_name3', 'la_name3', 'gr3', 3)
aspirants = [st1, st2, st3]
for el in aspirants:

    print(el.getScholarship())


#Задача 4
#Создать класс Animal и расширяющие его классы Dog, Cat, Horse.
# Класс Animal содержит переменные food, location и методы makeNoise, eat, sleep.

#Метод makeNoise, например, может выводить на консоль "Такое-то животное спит".
#Dog, Cat, Horse переопределяют методы makeNoise, eat.
#Добавьте переменные в классы Dog, Cat, Horse, характеризующие только этих животных.
#Создайте класс Ветеринар, в котором определите метод treatAnimal(animal).
# Пусть этот метод распечатывает food и location пришедшего на прием животного.
#Создайте список элементов типа Animal, в который запишите животных всех имеющихся у вас типов.
#В цикле отправляйте их на прием к ветеринару.

class Animal:

    def __init__(self, food, location):
        self.food = food
        self.location = location

    def makeNoise(self):
        print('The animal make noise.')

    def eat(self):
        print(f'The animal eat {self.food}.')

    def sleep(self):
        print('The animal sleep.')

class Dog(Animal):
    __name = 'Dog'
    def __init__(self, food, location):
        self.food = food
        self.location = location

    def makeNoise(self):
        print(f'The {self.__name} say Gav-gav')

    def eat(self):
        print(f'The animal eat {self.food}.')

    def hunter(self):
        print(f'The {self.__name} is a hunter.')


class Cat(Animal):
    __name = 'Cat'
    def __init__(self, food, location):
        self.food = food
        self.location = location

    def makeNoise(self):
        print(f'The {self.__name} say Mew-mew')

    def eat(self):
        print(f'The animal eat {self.food}.')

    def climb(self):
        print(f'The {self.__name} is climb a tree.')

class Horse(Animal):
    __name = 'Horse'
    def __init__(self, food, location):
        self.food = food
        self.location = location

    def makeNoise(self):
        print(f'The {self.__name} say I-go-go')

    def eat(self):
        print(f'The animal eat {self.food}.')

    def runner(self):
        print(f'The {self.__name} is a runner.')

class Vet():

    def treatAnimal(self, animal):
        print(f'{animal.food}, {animal.location}')


ann = Animal('Tree', 'Deli')
ann.makeNoise()

dog = Dog('Meat', 'Brest')
dog.makeNoise()

cat = Cat('Mouse', 'Minsk')
cat.makeNoise()

horse = Horse('Grass', 'Grodno')

vet = Vet()
vet.treatAnimal(cat)

animals = [dog, cat, horse]
for item in animals:
    vet.treatAnimal(item)



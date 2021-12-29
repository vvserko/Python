#Создать класс машина, имеющий марку, число цилиндров, мощность.
# Определить конструкторы, деструктор и функцию печати.
# Создать производный класс – грузовики, имеющий грузоподъемность кузова.
# Определить конструкторы , деструкторы, функцию печати.
# Определить функции переназначения марки и грузоподъемности.
import os

class Car:
    def __init__(self, mark, num_cilinder, power):
        self.__mark = mark
        self.__num_cilinder = num_cilinder
        self.__power = power


    def __del__(self):
        print("удален из памяти", self.__mark, self.__num_cilinder, self.__power)

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self,value):
        self.__mark = value

    @property
    def num_cilinder(self):
        return self.__num_cilinder

    @num_cilinder.setter
    def num_cilinder(self, value):
        self.__num_cilinder = value

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        self.__power = value

    def __str__(self):
        return f'Марка:{self.__mark}, {self.__num_cilinder} цилиндров, {self.__power} лошадиных сил'

    def __repr__(self):
        return f"Марка:{self.__mark}, {self.__num_cilinder} цилиндров, {self.__power} лошадиных сил"

class Truck(Car): # Создать производный класс – грузовики, имеющий грузоподъемность кузова.
    def __init__(self, mark, num_cilinder, power, carrying_carcase):
        self.__mark = mark
        self.__num_cilinder = num_cilinder
        self.__power = power
        self.__carrying_carcase = carrying_carcase

# Определить конструкторы , деструкторы, функцию печати.
    def __del__(self):
        print("удален из памяти", self.__mark, self.__num_cilinder, self.__power,self.__carrying_carcase)

    def __str__(self):
        return f'Марка:{self.__mark}, {self.__num_cilinder} цилиндров, {self.__power} лошадиных сил, {self.__carrying_carcase} грузоподъемность кузова тонн'

    def __repr__(self):
        return f"Марка:{self.__mark}, {self.__num_cilinder} цилиндров, {self.__power}) лошадиных сил, {self.__carrying_carcase} грузоподъемность кузова тонн"

    # Определить функции переназначения марки и грузоподъемности.
    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, value):
        self.__mark = value

    @property
    def carrying_carcase(self):
        return self.__carrying_carcase

    @carrying_carcase.setter
    def carrying_carcase(self, value):
        self.__carrying_carcase = value

lada = Car('Lada Priora', 16, 96)
print(lada)
man = Truck('MAN', 24, 440, 15)
print(man)
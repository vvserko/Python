import vvs.mymodule
class Person:
    def __init__(self, n: str, a: int):
        self.name = n
        self.__age = a

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, v):
        self.__age = v

    def __str__(self):
        return (f'{self.name},{self.__age}')

    def __repr__(self):
        return (f'group-{self.name},{self.__age}')



vova1 = Person('Serko Vladimir', 30)
vova2 = Person('Volk Vladimir', 25)
misha1 = Person('Strock Misha', 41)
print(vova1.age)
group = [vova1, vova2, misha1]
print(group)
group = sorted(group, key=lambda x: x.age)
for el in group:
    print(el)
print(vvs.mymodule.Umnozh.kor(vova1.age))

class Potok(Person):
    def sum_age(self, p):
        sum = 0
        for el in p:
            sum += el.age
        return sum

potok1 = Potok('группа', 4545)
potok2 = Potok('группа22', 66)
potoki = [potok1, potok2]
print(potoki)
print(potok1.sum_age(potoki))
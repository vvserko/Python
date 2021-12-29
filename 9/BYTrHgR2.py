class Cat:
    paws = 4

    def __init__(self, name:str, color:str):
        self.name = name
        self.color = color

    def count_paws(self):
        print(f'{self.name} : {self.paws}')

    def age(self, n):
        self.age = n

    def mew(self):
        print('Meeew ' + self.name)

boris = Cat('boris', 'black')
cat2 = Cat('cat2', 'green')
boris.paws = 4
Cat.paws = 2
boris.count_paws()
cat2.count_paws()











#Создайте структуру с именем student, содержащую поля:
# фамилия и инициалы, номер группы, успеваемость (массив из пяти элементов).
# Создать массив из десяти элементов такого типа, упорядочить записи по возрастанию среднего балла.
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.
class Student:

    def __init__(self, first_name, last_name, group_number, rating: list):
        self.group_number = group_number
        self.rating = rating
        self.last_name = last_name
        self.first_name = first_name
        self.personal_number = '00000'

    def set_personal_number(self, value):
        if len(value) >= 5:
            self.personal_number = value
        else:
            self.personal_number = '00000'

    def get_personal_number(self):
        return self.personal_number

    def get_is_perfect(self):
        flag = True
        for r in self.rating:
            if r < 4:
                flag = False
                break
        return flag

    def __str__(self):
        return f'{self.first_name} {self.last_name}: #{self.group_number}, {self.average()}'

    def __repr__(self):
        return f'{self.first_name} {self.last_name}: #{self.group_number}, {self.average()}'

    def average(self):
        return sum(self.rating)/len(self.rating)


student1 = Student('fS1', 'lS1', 123, [3, 3, 3, 4, 5])
student1.personal_number = '145'


student2 = Student('fS2', 'lS2', 13, [3, 3, 3, 4, 5])
student3 = Student('fS3', 'lS3', 23, [4, 4, 4, 4, 5])
student4 = Student('fS4', 'lS4', 233, [3, 3, 3, 4, 5])
student5 = Student('fS5', 'lS5', 153, [3, 3, 3, 4, 5])
students = [student1, student2, student3, student4, student5]

for s in students:
    if s.get_is_perfect():
        print(s)
# students = sorted(students, key=lambda student: student.average)


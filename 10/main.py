#Создайте структуру с именем train,
# содержащую поля: название пункта назначения, номер поезда, время отправления.
# Ввести данные в массив из пяти элементов типа train.
# Добавить возможность вывода информации о поезде, номер которого введен пользователем.
 
class Train:
 
    def __init__(self, destination, number, time):
        self.time = time
        self.number = number
        self.destination = destination
 
    def __str__(self):
        return f'Поезд № {self.number} - {self.time}'
 
 
train1 = Train('D1', 81, '10:20')
train2 = Train('D2', 12, '11:30')
train3 = Train('D3', 31, '16:40')
train4 = Train('D4', 11, '10:30')
train5 = Train('D5', 16, '10:30')
 
trains = [train5, train4, train3, train2, train1]
n = int(input('Please enter train number: '))
 
for t in trains:
    if t.number == n:
        print(t)
        break
else:
    print('no')
 
 
 
 
#########################
 
class Train:
 
    def __init__(self, destination, number, time):
        self.__time = time
        self.__num1 = number
        self.__destination = destination
 
    @property
    def num(self):
        return self.__num1
 
    @num.setter
    def num(self, value: int):
        self.__num1 = value
 
train = Train('D1', 81, '10:20')
 
train.num = 1111
print(train.num)
 
 
 
###################
 
# Описать класс, представляющий треугольник.
# Предусмотреть методы для создания объектов,
# вычисления площади,
# периметра.
# Описать свойства для получения состояния объекта.
 
class Triangle:
 
    def __init__(self, a, b, c):
        self._c = c
        self._b = b
        self._a = a
 
    def perimeter(self):
        return self._a + self._b + self._c
 
    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self._a) * (p - self._b) * (p - self._c)) ** 0.5
    
    
######################
 
#Создать класс Figure
# с методами вычисления площади и периметра, а также методом, выводящим информацию о фигуре на экран.
# Создать производные классы: Rectangle (прямоугольник), Circle (круг), Квадрат (square)
# Triangle (треугольник) со своими методами вычисления площади и периметра.
# Создать массив 4 фигур и вывести полную информацию о фигурах на экран.
import math
import turtle
pointer = turtle.Turtle()
pointer.speed('fastest')
 
class Point:
 
    def __init__(self, x, y):
        self.y = y
        self.x = x
 
class Figure:
 
    def __init__(self, start: Point):
        self.start = start
 
    def area(self):
        return 0
 
    def perimeter(self):
        return 0
 
    def draw(self):
        pass
 
    def display(self):
        pass
 
class Rectangle(Figure):
 
    def __init__(self, a, b, start):
        self.b = b
        self.a = a
        super().__init__(start)
 
    def area(self):
        return self.a * self.b
 
    def perimeter(self):
        return (self.a + self.b) * 2
 
    def display(self):
        return f'Прямоугольник a={self.a}, b={self.b}'
 
    def draw(self):
        pointer.setposition(self.start.x, self.start.y)
        pointer.pendown()
        for _ in range(2):
            pointer.forward(self.a)
            pointer.left(90)
            pointer.forward(self.b)
            pointer.left(90)
        pointer.penup()
 
class Square(Rectangle):
 
    def __init__(self, a, start):
        super().__init__(a, a, start)
 
    def display(self):
        return f'Квадрат a={self.a}'
 
class Circle(Figure):
 
    def __init__(self, r, start):
        super().__init__(start)
        self.r = r
 
    def area(self):
        return math.pi * self.r**2
 
    def perimeter(self):
        return 2 * math.pi * self.r
 
    def display(self):
        return f'Круг r={self.r}'
 
    def draw(self):
        pointer.setposition(self.start.x, self.start.y)
        pointer.pendown()
        pointer.circle(self.r)
        pointer.penup()
 
class Triangle(Figure):
 
    def __init__(self, a, b, c, start):
        self._c = c
        self._b = b
        self._a = a
        super().__init__(start)
 
    def perimeter(self):
        return self._a + self._b + self._c
 
    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self._a) * (p - self._b) * (p - self._c)) ** 0.5
 
    def display(self):
        return f'Треугольник a={self._a}, b={self._b}, c={self._c}'
 
    def draw(self):
        pointer.setposition(self.start.x, self.start.y)
        pointer.pendown()
        pointer.forward(self._a)
        pointer.left(120)
        pointer.forward(self._b)
        pointer.left(120)
        pointer.forward(self._c)
 
 
 
p = Point(0,0)
circle = Circle(100, p)
p2 = Point(300, 300)
square = Square(100,p2)
rectangle = Rectangle(100,200, p)
triangle = Triangle(300, 300, 300, p)
 
figures = (circle, square, rectangle, triangle)
 
for f in figures:
    print(f.display())
    f.draw()
 
turtle.mainloop()


# Класс Покупатель с полями Фамилия, Имя, Отчество, Адрес,
# Номер кредитной карточки, Номер банковского счета;
#
# Конструктор;
# Методы:
# установка значений атрибутов,
# получение значений атрибутов,
# вывод информации.
# Создать список объектов данного класса.
# Вывести список покупателей в алфавитном порядке
# Вывести список покупателей, у которых номер кредитной карточки находится в заданном диапазоне.
 
import random
 
class Customer:
 
    def __init__(self, name, address, card_number):
        self._card_number = card_number
        self._address = address
        self._name = name
 
    @property
    def name(self):
        return self._name
 
    @name.setter
    def name(self, value):
        self._name = value
 
    @property
    def card_number(self):
        return self._card_number
 
    @card_number.setter
    def card_number(self, value):
        self._card_number = value
 
    def __str__(self):
        return f'Customer: {self._name} - {self._card_number}'
 
    def __repr__(self):
        return f'Customer: {self._name} - {self._card_number}'
 
customers = []
 
for i in range(20):
    name = 'name' + str(random.randint(1, 1000))
    address = 'address' + str(random.randint(1, 1000))
    card_number = random.randint(1000, 9000)
    customer = Customer(name, address, card_number)
    customers.append(customer)
 
customers = sorted(customers, key=lambda c: c.name)
 
print(customers)
 
 
 
 
 
##########################################
 
# Создайте класс Date, который будет содержать информацию о дате (день, месяц, год).
# С помощью механизма перегрузки операторов, определите операцию разности
# двух дат (результат в виде количества дней между датами),
# а также операцию увеличения даты на определенное
# количество дней.
 
class Date:
 
    def __init__(self, days, months, years):
        self._years = years
        self._months = months
        self._days = days
 
    def __call__(self, *args, **kwargs):
        return 'hello'
 
    @property
    def days(self):
        return self._days + self._months * 30 + self._years * 12 * 30
 
    @property
    def months(self):
        return self._months + self._years * 12
 
    @property
    def years(self):
        return self._years
 
    def __str__(self):
        return f'{self._days} {self._months} {self._years}'
 
    def __repr__(self):
        return self.__str__()
 
    def sum(self, date):
        all_days = self.days + date.days
        y = int(all_days / (12*30))
        m = int((all_days % y) / 30)
        d = all_days - m * 30 - y * 12 * 30
        return Date(d,m,y)
 
    def __add__(self, other):
        if isinstance(other, Date):
            return self.sum(other)
        else:
            date = Date(other, 0, 0)
            return self.sum(date)
 
 
date1 = Date(1, 1, 2020)
date2 = Date(1, 1, 2021)
res = date1 + 100
print(res)

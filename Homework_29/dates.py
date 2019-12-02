#Класс с одним атрибутом, который принимает строку в формате '05-01-1991'. Это год рождения. При инициализации нужно проверить, является ли эта дата валидной и написать property которая по этим данным говорит, сколько ему лет.

#Задание номер два, написать проперти которое считает количество прожитих высокосных лет

import datetime
from datetime import date

class ParentClass:
    def __init__(self, name, string):
        self.name = name
        self.string = self._validate_date(string)
    def _validate_date(self, date):
        try:
            return self.date_format(date)
        except ValueError:
            raise ValueError("Incorrect date type")

    @property
    def age(self):
        today = date.today()
        delta = today - self.string.date()
        age = today.year - self.string.year - ((today.month, today.day) < (self.string.month, self.string.day))
        if delta.days < 0:
            raise Exception('Please input correct date, it cannot be in Future')
        return f'{self.name} is {age} years old'

    @property
    def leap_years(self):
        array = range(self.string.year, date.today().year)
        answer = 0
        for year in array:
            if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
                answer = answer + 1
        return f'Number of leap years: {answer}'

    @staticmethod
    def date_format(string):
        return datetime.datetime.strptime(string, '%d-%m-%Y')

myclass = ParentClass('Bogdan', '03-12-1644')

print(myclass.age)

print(myclass.leap_years)
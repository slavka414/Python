# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):
        self.d = data

    @classmethod
    def set_date(cls, data):
        for i in data[0]:
            if ord(i) < 48 or ord(i) > 57:          #Правильность дня
                return "Неправильное число"
        for i in data[1]:
            if ord(i) < 48 or ord(i) > 57:          #Правильность месяца
                return "Неправильный месяц"
        for i in data[2]:
            if ord(i) < 48 or ord(i) > 57:          #Правильность года
                return "Неправильный год"
        if int(data[1]) > 12:                       #Правильность количества месяцев
            return "В году не может быть больше 12 месяцев"
        if int(data[2]) % 4 == 0 and int(data[1]) == 2 and int(data[0]) > 29:           #Правильность високосного года
            return "Это год високосный, в феврале только 29 дней"
        if int(data[2]) % 4 != 0 and int(data[1]) == 2 and int(data[0]) > 28:           #Правильность невисокосного года
            return "Это год невисокосный, в феврале только 28 дней"
        if int(data[1]) == 1 or int(data[1]) == 3 or int(data[1]) == 5 or int(data[1]) == 7 or int(data[1]) == 8 or int(data[1]) == 10 or int(data[1]) == 12:
            if int(data[0]) > 31:
                return "В этом месяце 31 день"
        if int(data[1]) == 4 or int(data[1]) == 6 or int(data[1]) == 9 or int(data[1]) == 11:
            if int(data[0]) > 30:
                return "В этом месяце 30 день"


        print(type(data[1]))
        return data

    @staticmethod
    def get_date(obj):
        try:
            obj = obj.split("-")
            day = obj[0]
            month = obj[1]
            year = obj[2]
        except ValueError:
            print("Error")
        return day, month, year

DATA = ("02-04-2021")
# print(type(DATA))
print(Data.get_date(DATA))
print(Data.set_date(Data.get_date(DATA)))

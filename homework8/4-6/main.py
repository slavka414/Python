# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class sclad:
    pass

class orgtex:
    def __init__(self, name, kol_vo, price):
        self.name = name
        self.kolvo = kol_vo
        self.price = price
        print(name, kol_vo, price)

class printer(orgtex):
    def __init__(self, name, kol_vo, price, type, cvet=True):
        super().__init__(name, kol_vo, price)
        self.cvet = cvet
        self.type = type
        print(self.name, self.kolvo, self.price, type, cvet)

class scaner(orgtex):
    def __init__(self, name, kol_vo, price, format):
        super().__init__(name, kol_vo, price)
        self.format = format
        print(self.name, self.kolvo, self.price, format)

class kseroks(orgtex):
    def __init__(self, name, kol_vo, price, scorost):
        super().__init__(name, kol_vo, price)
        self.scorost = scorost
        print(self.name, self.kolvo, self.price, scorost)

xerox = kseroks("xerox", "1 sht", "1000 rub", "5 listov")
hp = scaner("HP", "2 sht", "500 rub", "A3")
canon = printer("Canon", "3 sht", "2000 rub", "laser", True)

new = []

while True:
    new_perif = input("Введите тип устройства (1 - принтер, 2 - сканер, 3 - копир):  ")
    if new_perif == "1":
        new.append(input("Введи незвание принтера:  "))

        while len(new) == 1:
            new_kolvo = input("Введи количество принтеров:  ")
            for i in new_kolvo:
                if ord(i) > 47 and ord(i) < 58:
                    new.append(new_kolvo)
                else:
                    print(" Error")
                break

        while len(new) == 2:
            new_price = input("Введи стоимость принтера:  ")
            for i in new_price:
                if ord(i) > 47 and ord(i) < 58:
                    new.append(new_price)
                else:
                    print(" Error")
                break

        while len(new) == 3:
            new_type = input("Лазерный(1) или струйный(2):  ")
            if new_type == "1":
                new.append("Laser")
            elif new_type == "2":
                new.append("Stryiniy")
            else:
                print(" Error")
                continue

        while len(new) == 4:
            new_cvet = input("Цветной (1=True) или нет (2=False):  ")
            if new_cvet == "1":
                new.append(True)
            elif new_cvet == "2":
                new.append(False)
            else:
                print(" Error")
                continue
            break
        print("Добавлен новый принтер: ")
        printer(new[0], new[1], new[2], new[3], new[4])
        break


    elif new_perif == "2":
        new.append(input("Введи незвание сканера:  "))

        while len(new) == 1:
            new_kolvo = input("Введи количество сканеров:  ")
            for i in new_kolvo:
                if ord(i) > 47 and ord(i) < 58:
                    new.append(new_kolvo)
                else:
                    print(" Error")
                break

        while len(new) == 2:
            new_price = input("Введи стоимость сканеров:  ")
            for i in new_price:
                if ord(i) > 47 and ord(i) < 58:
                    new.append(new_price)
                else:
                    print(" Error")
                break

        while len(new) == 3:
            new_format = input("Введете формат сканера:  ")
            if new_format == "A0":
                new.append("A0")
            elif new_format == "A1":
                new.append("A1")
            elif new_format == "A2":
                new.append("A2")
            elif new_format == "A3":
                new.append("A3")
            elif new_format == "A4":
                new.append("A4")
            elif new_format == "A5":
                new.append("A5")
            else:
                print(" Error")
                continue
        print("Добавлен новый сканер: ")
        scaner(new[0], new[1], new[2], new[3])
        break


    elif new_perif == "3":
        new.append(input("Введи незвание копира:  "))

        while len(new) == 1:
            new_kolvo = input("Введи количество копира:  ")
            for i in new_kolvo:
                if ord(i) > 47 and ord(i) < 58:
                    new.append(new_kolvo)
                else:
                    print(" Error")
                break

        while len(new) == 2:
            new_price = input("Введи стоимость копира:  ")
            for i in new_price:
                if ord(i) > 47 and ord(i) < 58:
                    new.append(new_price)
                else:
                    print(" Error")
                break

        while len(new) == 3:
            new_price = input("Введи скорость печати копира:  ")
            for i in new_price:
                if ord(i) > 47 and ord(i) < 58:
                    new.append(new_price)
                else:
                    print(" Error")
                break

        print("Добавлен новый ксерокс: ")
        kseroks(new[0], new[1], new[2], new[3])
        break
    else:
        print(" Error")
        continue




# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.ip = bool(is_police)
        self.s = speed
        self.c = color
        self.n = name

    def go(self):
        print(f"{self.c} {self.n} поехала cо скоростью {self.s}км/ч")

    def stop(self):
        print(f"{self.c} {self.n} остановилась")

    def turn(self, direction):
        print(f"{self.c} {self.n} повернула {direction}")

class TomnCar(Car):
    def speed_of_car(self, show_speed):
        self.ss = show_speed
        if self.ss > 60:
            print("Превышение скорости")

class Workcar(Car):
    def speed_of_car(self, show_speed):
        self.ss = show_speed
        if self.ss > 40:
            print("Превышение скорости")

car_1 = Car(90, "yelow", "Kia", False)
car_1.go()
car_1.stop()
car_1.turn("left")

car_2 = TomnCar(30, "black", "VW", False)
car_2.go()
car_2.speed_of_car(61)

car_3 = Workcar(20, "green", "Lada", True)
car_3.go()
car_3.speed_of_car(41)


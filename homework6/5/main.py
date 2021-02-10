# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title, draw):
        self.t = title
        self.d = draw
        print(f'Запуск отрисовки {self.t}')

class Pen(Stationery):
    def draw(self, draw):
        self.d = draw
        print(f'Рисуешь {self.t}, цвет {self.d}')

class Pencil(Stationery):
    def draw(self, draw):
        self.d = draw
        print(f'Рисуешь {self.t}, цвет {self.d}')

class Handle(Stationery):
    def draw(self, draw):
        self.d = draw
        print(f'Рисуешь {self.t}, цвет {self.d}')

office_supplies_1 = Pen("Pen", "yelow")
office_supplies_1.draw("yelow")
office_supplies_2 = Pencil("Pencil", "black")
office_supplies_2.draw("black")
office_supplies_3 = Handle("Handle", "green")
office_supplies_3.draw("green")



# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
# [   (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})           ]
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
# Пример:
# {   “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]                                         }
number_dict = 1             #счетчик при записи в словарь (был 0)
number_ast = 0              #
number_asd = 0              #
dict_all = {}
list = []
num = 1                     #счетчик позиции при выдачи структуры
number = 0                  # счетчик позиций при вводе
while True:
    answer1 = str(input('Хотите добавить товар (y), посмотреть структуру (s), посмотреть аналитику (a) или выйти (n):  '))
    tupple = ("название", "цена", "количество", "единицы")

    if answer1 == 'y':
        number += 1
        name = str(input('Введите название товара:   '))
        price = str(input('Введите цену товара:   '))
        items = str(input('Введите количество товара:   '))
        units = str(input('Введите единицы товара:   '))
        dict_all.update({number_dict: name})
        number_dict += 1
        dict_all.update({number_dict: price})
        number_dict += 1
        dict_all.update({number_dict: items})
        number_dict += 1
        dict_all.update({number_dict: units})
        number_dict += 1
        print(dict_all)
        member = number

    elif answer1 == 's':
        number_ast = 0
        number_asd = 1
        number = member
        num = 1
        while number > 0:
            print(f'{num}. {tupple[number_ast]}: {dict_all[number_asd]} {tupple[number_ast + 1]}: {dict_all[number_asd + 1]} {tupple[number_ast + 2]}: {dict_all[number_asd + 2]} {tupple[number_ast + 3]}: {dict_all[number_asd + 3]}')
            number_asd += 4
            number_ast = 0
            num += 1
            number -= 1

    elif answer1 == 'a':
        number_ast = 0
        number_asd = 1
        number = member
        while number > 0:
            x = number_dict
            x = x // 4
            while x > 0:
                list.append([dict_all[number_dict - (number_dict // x)]])
                x -= 1
                if x == 0:
                    list.append([dict_all[number_dict]])
                    break
            cor = (tupple[number_ast], list)
            print(cor)
            list.clear()
#            print(f'{tupple[number_ast]}: {dict_all[number_asd]}  ')
#            if number_dict % 4 == 0:
#                number_dict //= 4
#                while True:
#                    print(f'{tupple[number_dict]}: {dict_all[number_dict]}  ')
#                    number_dict -= 1
            number_ast += 1
            number_asd += 1
            number -= 1



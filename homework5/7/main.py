# Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json
all_firm = {}
profit = 0
k = 0
string = []
with open("text_7.txt", "r", encoding="utf-8") as text:
    for line in text:
        list = line.split()
        summa = int(list[2]) - int(list[3])
        all_firm.update({list[0]: summa})
        if summa > 0:
            k +=1
            profit += summa
            continue
    profit = profit / k
    string = [all_firm, {"avarage_profit": profit}]

print(string)

with open("file.json","w", encoding="utf-8") as text_j:

    string_j = json.dumps(string, indent=4, ensure_ascii=False)
    print(string_j)
    json.dump(string_j, text_j)



# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
#list1 = [4, 7, 1, 3, 2, 99, 10, 6, 77]
list1 = []
count = 0
count2 = 0

while True:
    answer = str(input(' Хочешь ввести новый элемент списка (y/n):  '))
    if answer == 'y' or answer == 'Y':
        print('1')
        new_el = int(input('Вводи:   '))
        list1.append(new_el)
        print(list1)
        count += 1

    elif answer == 'n' or answer == 'N':
        print('2')
        break
    else:
        print('3')
        break
print(f'Количество компонентов:  {count}')

first = 0
second = 0
while count2 <= count:
    first = list1[count2]
    count2 += 1
    if count2 >= count:
        break
    second = list1[count2]
    count2 += 1
    list1.pop(count2 - 2)
    list1.pop(count2 - 2)
    list1.insert(count2 - 2, second)
    list1.insert(count2 - 1, first)
print(list1)






# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

list = [7, 5, 3, 3, 2]

print(list)
tsil = list[::-1]
print(tsil)
while True:
	answer = str(input('Хочешь ввести число(y/n): '))
	if answer == 'y' or answer == 'Y':
		number = int(input('Введите число '))
		for i in list:
			count = int(list.index(i))
			if number == i:
				list.insert(count, number)
				print(f'Пользователь ввёл число {number}. Результат: {list}')
				break
			elif number > i:
				list.insert(count, number)
				print(f'Пользователь ввёл число {number}. Результат: {list}')
				break
			elif number < i and count + 1 == len(list):                             #условие для 1
				list.insert(count + 1, number)
				print(f'Пользователь ввёл число {number}. Результат: {list}')
				break
			elif number < i:
#				list.insert(count, number)
#				print(f'Пользователь ввёл число {number}. Результат: {list}')
				continue

	else:
		break


print(list)


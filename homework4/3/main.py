# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.

twenty = {el for el in range(20, 240, 20)}
print(twenty)

twenty_one = {el for el in range(21, 240, 21)}
print(twenty_one)

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

text_en = open("text_4.txt", 'r', encoding="utf-8")
text_ru = open("text_ru.txt", "w", encoding="utf-8")
num_en = []
str = []

for i in text_en:
    str = (i.split())
    if str[0] == 'One':
        text_ru.writelines('Один' + str[1] + str[2] + '\n')
    if str[0] == 'Two':
        text_ru.writelines('Два' + str[1] + str[2] + '\n')
    if str[0] == 'Three':
        text_ru.writelines('Три' + str[1] + str[2] + '\n')
    if str[0] == 'Four':
        text_ru.writelines('Четыре' + str[1] + str[2] + '\n')

text_en.close()
text_ru.close()
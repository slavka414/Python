# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

text = open("text.txt", "w")
word = []
while True:

    word = input('Вводите:   ')
    if len(word) > 0:
        text.writelines(word + '\n')
    elif len(word) == 0:
        text.close()
        break
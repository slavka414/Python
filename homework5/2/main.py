# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

text = open("text.txt", "w")
word = []
count = 0
while True:

    word = input('Вводите:   ')
    if len(word) > 0:
        x = word.count(" ") + 1
        text.writelines(word + " " + str(x) + '\n')
        if x == 1:
            print(f'{x} слово')
        elif x >= 2 and x <= 4:
            print(f'{x} слова')
        else:
            print(f'{x} слов')
        count += 1
    elif len(word) == 0:
        text.writelines(str(count) + '\n')
        text.close()
        print(f'{count} строк')
        break

# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

str = str(input())
print(str)
count = int(str.count(' '))
print(f'Количество слов:   {count + 1}')

str_cor = (str.split())
print(str_cor)

i = 0
while i <= count:
    if len(str_cor[i]) > 10:
        str10 = str_cor[i]
        print(f'{i + 1}.  {str10[:10]}')
        i += 1
        continue
    print(f'{i + 1}.  {str_cor[i]}')
    i += 1

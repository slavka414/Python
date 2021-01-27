# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран

text = open("text.txt", "w")
num = 0
sum = 0
try:
    while num >= 0:
        num = int(input('Введите число (если ввести букву программа подсчитает сумму чисел):  '))
        sum += num
        text.write(str(num) + ' ')
except ValueError:
    print(sum)
    text.write('\n' + str(sum))

text.close()
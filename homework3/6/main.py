# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

st = str(input('Введите слово:   '))


def line(string):
    print(list(string.lower()))
    for i in list(string.lower()):
        if ord(i) >= 97 ^ ord(i) <= 122:
            # return string.title()
            print(i)
        else:
            break

    return string.title()


print(line(st))

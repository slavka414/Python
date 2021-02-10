# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

# class comp_num:
#     def __init__(self, number1, number2):
#         self.num1 = number1
#         self.num2 = number2
#
#     def __add__(self, other):
#         return complex(self.num1, self.num2), complex(other.num1, other.num2)
#
# comp_a = (3, 2)
# comp_b = (5, 7)
# # print(type(comp_b[1]))
# # print(type(comp_b))
# print(comp_num(comp_a, comp_b))
#
# # comp_a = complex(3, 2)
# # comp_b = complex(5, 7)


class comp_num:
    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2

    def __add__(self, other):
        sum_a = self.num1 + other.num1
        sum_b = self.num2 + other.num2
        multiplications_a = self.num1 * other.num1 + ((self.num2 * other.num2) * (-1))
        multiplications_b = (self.num1 * other.num2) + (other.num1 * self.num2)
        return f"Сумма комплексных чисел:  {complex(sum_a, sum_b)}, Произведение комплексных чисел:  {complex(multiplications_a, multiplications_b)}"

comp_a = comp_num(3, 2)
comp_b = comp_num(5, 7)
print(comp_a + comp_b)
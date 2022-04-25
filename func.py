# def hello():
#     print("Hello Word")
#     print(10 + 10)
#     print(10 * 2)
# hello()

# def add():
#     num1 = int(input("Num1: "))
#     num2 = int(input("Num2: "))
#     print(num1 + num2)
# add()

# #Здесь работает только "тело" функции
# def sub(num1, num2):
#     print(10 + 10)
# sub(100, 10)

# def sub(num1, num2):
#     print(num1 - num2)
# sub(100, 10)

# def math():
#     numbers = [i for i in range(1000)]
#     for i in numbers:
#         if i % 2 == 0:
#             print(i)
# math()

# def info(name = "Ivan", surname = "Ivanov"):
#     print(f"Имя {name}, фамилия {surname}")
# info("Muntasir", "Tolbaev")
# info("Faha", "Hi")

# Создать функцию calc(a, b, operation). Описание входных параметров:
# Первое число(дробное число)
# Второе число(дробное число)
# Действие над ними:
#    1) + Сложить
#    2) - Вычесть
#    3) * Умножить
#    4) / Разделить
#    Сделайте момент где если пользователь делит число на 0, нужно вывести “На    ноль делить нельзя”
#    В остальных случаях функция должна возвращать "Операция не поддерживается

# def calc(a, b, operation):
#     if operation == "+":
#         print(a + b)
#     elif operation == "-":
#         print(a - b)
#     elif operation == "*":
#         print(a * b)
#     elif operation == "/":
#         try:
#             print(a / b)
#         except ZeroDivisionError:
#             print("На    ноль делить нельзя")
#     else:
#         print("Операция не поддерживается")
# calc(10, 5, "**")
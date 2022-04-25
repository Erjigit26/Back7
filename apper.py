# print("Hello world")
# print(1 + 1)
# print(2 - 1)
# print(2 * 2)
# print(int(4 / 2))
# print(7 // 2)
# print(7 % 3)
# print(3 ** 4)

# print(6 == 8)
# print(5 != 2)
# print(2 > 4)
# print(9 < 4)
# print(1 >= 3)
# print(2 <= 3)
# print(2 == 4)
# print(2==2)
# print(4>3)
# print(8<7)
# print(10/2>4)
# print(2>5*2)
# print(2!=4)

# number = 10
# print(number*2)

# name = "John"
# surname = "Doe"
# print(name+surname)

# name = "Mark"
# surname = "Twain"
# print(name+"  "+surname)

# name, surname, age = "John", "Doe", 20
# print(age)

# num1 = 10
# num2 = 20
# num1, num2 = num2, num1
# print(num1)


# Написать функцию, которая принимает много цифр (...) и умножает их на 2.

# def two(*nums):
#     for i in nums:
#         print(i * 2)

# two(1, 2, 3, 4, 5, 6)

# Написать функцию, которая принимает ... в мы туда передаем страны, то есть в key английское название, а в value русское название 

# def country(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# country(USA = "США", Russia = "Россия", Kyrgyzstan = "Кыргызстан")

# написать функцию lexus, которая принимает …,  в аргументах передаем его технические характеристики. Все это вывести.

# def lexus(**settings):
#     for key, value in settings.items():
#         print(key, value)

# lexus(volume = 3.5, color = "white", year = 2021, type = "SUV")

# Напишите функцию -- чат-бот, который 
# a. Всегда отвечает “Конечно!” на любой вопрос 
# b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК! 
# c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же духе!” Если вызвал функцию, но ничего не передал. 
# d. В любых других случаях, отвечает “ну и что”

# def chat_bot(message):
#     if message == "":
#         print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#     elif message == str.upper(message):
#         print("Успокойся")
#     elif message:
#         print("Конечно")
#     else:
#         print("ну и что")

# chat_bot("ВЫ!")

# lst = [] 
# for i in range(10): 
#     if i % 2 == 0: 
#         lst.append(i) 
# print(lst) 

# lst = [i for i in range(10) if i % 2 == 0]
# print(lst)

# cars = ["Bmw", "Mersedes", "Lexus", "Kia", "Lada"] 
# new_cars = [] 
# for x in cars: 
#     if "a" in x: 
#         new_cars.append(x) 
# print(new_cars) 

# cars = ["Bmw", "Mersedes", "Lexus", "Kia", "Lada"] 
# new_cars = [ x for x in cars if  "a" in x]
# print(new_cars)

# squares = [] 
# for i in range(10): 
#     squares.append(i) 
# print(squares)

# squares = [i for i in range(10) ]
# print(squares)

# a = [1, 2, 3, 4, 5]
# # b = []
# # for num in a:
# #     b.append(num)
# # print(b)

# c = [num * 2 for num in a]
# print(c)

# range3 = [num * 3 for num in range(1, 6)]
# print(range3)

# range_elements = []
# for num in range(1, 6):
#     a = num * 3
#     range_elements.append(a)
# print(range_elements)

# a = [1, 10, 12, 4, 3, 20, 55]
# a_filtered = []
# for num in a:
#     if num < 10:
#         a_filtered.append(num)
# print(a_filtered)

# a_filtered = [num for num in a if num < 10]
# res = ['chetnoye' if 4 % 2== 0 else "nechet"]
# print(res)
# print(a_filtered)

# a_filtered_squared = [num ** 2 for num in a if num < 10]
# print(a_filtered_squared)

# wordss = ['hello', 'world', 'goodbye', 'privet', 'piano', 'qwertyuiopasd']
# # words_filtered = [word for word in words if len(word) < 6]
# # print(words_filtered)

# words = [word + '.' for word in wordss if len(word) == 13]
# print(words)


# a = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 56, 70, 'fourth', -50]
# d = {}
# b = None

# for el in a:
#     if type(el) == str:
#         d[el] = []
#         b = el
# # print(d)
#     else:
#         d[b].append(el)
# print(d)

# a, b, d = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 56, 70, 'fourth', -50], {}, None

# print(4, 5, end='hello')
# print(1, 2, 3, sep='!')

# rubles = 10
# kop = 99
# print("У меня есть %s рублей %s копеек" %(rubles,kop))

# a=float(input("Введите значение: "))
# b=float(input("Введите значение: "))
# c=float(input("Введите значение: "))
# p=a+b+c

# a=2
# b=7
# b=a
# a=b
# print(a,b)

# def main():
#     oper = input('символ(+,-,*,/):')
#     if oper != '+' and oper != '-' and oper != '*' and oper != '/':
#         print("пжл введите действительный символ")
#     else:
#         while True:
#             try:
#                 var1 = int(input("1: ")) 
#                 var2 = int(input("2: ")) 
#             except ValueError:
#                 print("Пжл введите только цифры")
#                 continue
#             else:
#                 break
#         if oper == "+":
#             print(var1 + var2)
#         elif oper == "-":
#             print(var1 - var2)
#         elif oper == "*":
#             print(var1 * var2)
#         elif oper == "/":
#             try:
#                 print(var1 / var2)
#             except ZeroDivisionError:
#                 print("На ноль делить нельзя")
# while True:
#     main()

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

# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")


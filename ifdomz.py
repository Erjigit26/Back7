# 1) Дано два числа. Вывести на экран наибольшее из чисел;
# Ответ:
# num1 = 500
# num2 = 600
# if num1 > num2:
#     print(num1)
# else:
#     print(num2)

# 1.2) Проверка на отрицательные и положительные числа
# Ответ
# num = int(input("Введите число: "))
# if num > 0:
#     print("Положительное")
# else:
#     print("Отрицательное")

# 1.5) Если вводится отрицательное число, перевести его в положительное
# Ответ
# num = int(input("Введите число: "))
# if num < 0:
#     print(-num)
# else:
#     print(num)

# 2) Пользователь вводит два числа с клавиатуры.
#  Вывести на экран yes, если они отличаются друг от друга, иначе вывести на экран No;
# Ответ
# num1 = input("Введите число: ")
# num2 = input("Введите следующее число: ")
# if num1 != num2:
#     print("yes")
# else:
#     print("No")

# 3) Дано число. Если оно больше 100 или меньше -100, то вывести на экран символ —, 
# иначе вывести на экран символ +;
# Ответ
# num = int(input("Введите число: "))
# if num > 100 or num < -100:
#     print("-")
# else:
#     print("+")

# 4) Пользователь вводит номер месяца (от 1 до 12). Вывести название сезона года на 
# экран (зима, весна, лето, осень);
# Ответ
# num = int(input("Введите число: "))
# if num == 12 or num == 1 or num == 2:
#     print("Зима")
# elif num == 3 or num == 4 or num == 5:
#     print("Весна")
# elif num == 6 or num == 7 or num == 8:
#     print("Лето")
# elif num == 9 or num == 10 or num == 11:
#     print("Осень")
# else:
#     print("Введите правильное число!")

# 5) Пользователь вводит три числа. Если все числа больше 10, то вывести на экран yes, иначе no
# Ответ
# num1 = int(input("Введите число: "))
# num2 = int(input("Введите следующее число: "))
# num3 = int(input("Введите последнее число: "))
# if num1 > 10 and num2 > 10 and num3 > 10:
#     print("yes")
# else:
#     print("no")

# 6) Дано три числа. Найти количество положительных чисел среди них
# Ответ
# num1 = input("Введите число: ")
# num2 = input("Введите следующее число: ")
# num3 = input("Введите последнее число: ")
# print(f'{3-(num1+num2+num3).count("-")}')

# 7) Пользователь вводит количество месяцев и лет. Вывести на экран количество дней 
# за это время. Считать, что в каждом месяце 29 дней;
# Ответ
# year = int(input("Введите год: "))
# month = int(input("Введите месяц: "))
# result = (year * 348) + (month * 29)
# print(result, "дней за это время прошло")

# 9) Напишите программу отбора в военкомат. Если Алмазу меньше 16ти лет то должно вывести 
# "еще рано", если 18 и выше то вывести "идем служить", 
# а если возраст равна 40 и выше то вывести "уже не надо"
# Ответ
# age = int(input("Age: "))
# if age < 16:
#     print("Еще рано")
# elif age >= 18 and age < 40:
#     print("Идём служить")
# elif age >= 40:
#     print("Уже не надо")


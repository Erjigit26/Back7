# a = 100
# b = 10
# # [when_true] if [codition] else [when_false]
# res = "А больше всех" if a > b else "А меньше всех"
# print(res)

# a = 100
# b = 10
# print("А больше всех" if a > b else "А меньше всех")

# a = 100
# b = 10
# c = 1000
# print("А больше всех" if c > a and c > b  else "С больше всех")

# a = 100
# b = 10
# c = 1000
# res = a if a > b and a > c else b if b > a and b > c else c
# print(res)

# a = 100
# b = 10
# c = 1000
# print(a if a > b and a > c else b if b > a and b > c else c)

# a, b, c, d = 100, 10, 1000, 5000
# print(a if a > b and a > c and a > d else b if b > a and b > c and b > d else c if c > a and c > b and c > d else d )

# number = int(input("Number: "))
# if number % 2 == 0:
#     print("Чeтное")
# else:
#     print("Нечетное")

# number = int(input("Number: "))
# print("Чeтное" if number % 2 == 0 else "Нечетное")

# # (when_true, when_false)[codition] с помощью кортежа(tuple)
# number = int(input("Number: "))
# print(("Чeтное", "Нечетное")[number % 2])

# my_passwords = ["qwerty", "12345678"]
# user_input = input("Введите пароль: ")
# if user_input in my_passwords:
#     print("Пароль верный")
# else:
#     print("Неверный пароль")

# my_passwords = ["qwerty", "12345678"]
# user_input = input("Введите пароль: ")
# print("Пароль верный" if user_input in my_passwords else "Неверный пароль")

# my_passwords = ["qwerty", "12345678"]
# user_input = input("Введите пароль: ")
# print(("Пароль верный", "Неверный пароль")[user_input in my_passwords])

# age = int(input("Возраст: ")) 
# if age >= 18 and age <= 50: 
#     print("Доступ разрешен") 
# elif age > 50: 
#     print("Вы уже старый") 
# else: 
#     print("Иди домой")

# age = int(input("Возраст: "))
# print("Доступ разрешен" if age >= 18 and age <= 50 else "Иди домой" and "Вы уже старый" if age > 50 else "Иди домой")

# name = input("Ваше имя: ") 
# names = ["Mark", "Kate", "Anna", "Smit"] 
# if name in names: 
#     print(f"{name} в нашем классе") 
# else: 
#     print(f"{name} не в нашем классе") 

# name = input("Ваше имя: ") 
# names = ["Mark", "Kate", "Anna", "Smit"] 
# print(f"{name} в нашем классе" if name in names else f"{name} не в нашем классе")


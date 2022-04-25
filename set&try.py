# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Аллё! На ноль делить нельзя")

# try:
#     print(10 + "Hello")
# except BaseException:
#     print("У вас ошибка! Знаете почему?")

# heloo = "Hi"
# try:
#     print(hi)
# except NameError:
#     print("Ошибка в названии - Эржигит")
# finally:  #не зависит от ошибки и выводит
#     print("В итоге")

# raise NameError("У вас ошибка - Эржигит")

# raise SyntaxError("У вас ошибка - Эржигит! Знаете почему?")

# raise TypeError("У вас ошибка - Эржигит")


# names = ["Kurmanbek", "Ali", "Bekzat", "Muntasir", "Kurmanbek"]
# print(set(names))

# cars = {"Audi", "BMW", "TESLA", "Rolls Royce"}
# cars.add("Lexus")
# print(cars)
# cars.pop()
# print(cars)
# cars.remove("TESLA")
# print(cars)
# for i in cars:
#     print(cars)

# cars = frozenset({"Audi", "BMW", "TESLA", "Rolls Royce", "Lexus"})
# print(cars)
# for i in cars:
#     print(i)

# numbers = []
# for i in range(1, 100001):
#     numbers.append(i)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# numbers = [1, 2, 3, 4, 5]
# numbers1 = max(numbers)
# numbers2 = min(numbers)
# numbers1, numbers2 = numbers2, numbers1
# print(numbers)
# student = {15 : "Muntasir", "age" : 18, "study" : "IT RUN", True : 10.5, (1, 2, 3, 4) : "Hello"}
# print(student)

# student = dict(name = "Muntasir", age = 18, study = "IT RUN")
# print(student) #второй способ создания словаря

# student = {"Name" : "Muntasir", "age" : 18, "study" : "IT RUN"}
# del student["age"] #удаление элемента с словаряб, с помощью оператора del
# print(student)

# print(student["age"])

# student.setdefault("Hello", "IT")
# student.pop("Name")
# print(student)

# student = {"Name" : "Muntasir", "age" : 18, "study" : "IT RUN"}
# student['study'] = "OSH MU"
# student['colour'] = "White"
# print(student.keys())
# print(student.values())
# print(student.get('color'))
# print(student.items())
# student.clear()
# print(student)
# for i in student.items():
#     print(i)
# for key,value in student.items():
#     print(key,value)

# marks = {'Physics':67, 'Maths':87}
# internal_marks = {'Practical':48}
# marks.update(internal_marks)
# print(marks)

# contact = {"Muntasir" : "0777777777"}
# while True:
#     command = input("1 - искать, 2 - добавить, 3 - удалить, 4 - обновить номер, 5 - посмотреть все контакты:")
#     if command == "1":
#         find_num = input("Какой контакт вы хотите найти?")
#         if find_num in contact:
#             print("Есть", contact[find_num])
#         else:
#             print("Такого нету")
#     elif command == "2":
#         add_name = input("Кого добавить?")
#         add_num = input("Введите номер: ")
#         contact.setdefault(add_name, add_num)
#         print("Контакт успешно добавлен")
#     elif command == "3":
#         delet_name = input("Кого хотите удалить?")
#         if delet_name in contact:
#             contact.pop(delet_name)
#             print("Контакт успешно удален")
#         else:
#             print("Такого нету")
#     elif command == "4":
#         contact_update = ("Вы хотите обновить?")
#         num_update = ("На какой номер хотите изменить?")
#         if contact_update in contact:
#             contact[contact_update] = num_update
#             print("Номер успешно обновлен")
#         else:
#             print(f"Такого {contact_update} контакта нет")
#         print("Контакты обнавлены")
#     elif command == "5":
#         print(contact)
#     else:
#         print("Ошибочная команда")
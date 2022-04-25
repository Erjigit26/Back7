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



# contact = {"Muntasir" : "0777777777"}
# while True:
#     command = input("1 - искать, 2 - добавить, 3 - удалить, 4 - обновить номер, 5 - посмотреть все контакты:")
#     if command == "1":
#         find_num = input("Какой контакт вы хотите найти?")
#         if find_num.title() in contact:
#             print("Есть", contact[find_num.title()])
#         else:
#             print("Такого нету")
#     elif command == "2":
#         add_name = input("Кого добавить?")
#         add_num = input("Введите номер: ")
#         contact.setdefault(add_name.title(), add_num)
#         print("Контакт успешно добавлен")
#     elif command == "3":
#         delet_name = input("Кого хотите удалить?")
#         if delet_name.title() in contact:
#             contact.pop(delet_name.title())
#             print("Контакт успешно удален")
#         else:
#             print("Такого нету")
#     elif command == "4":
#         update_name = input("Кого хотите обновить?")
#         if update_name in contact:
#             update_num = input("Обновновленный номер: ")
#             contact[update_name] = update_num
#             print("Номер успешно обновлен")
#         else:
#             print("Такого контакта нет")
#     elif command == "5":
#         for name, number in contact.items():
#             print(name, number)
#     else:
#         print("Ошибочная команда")

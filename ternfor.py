# num = []
# for i in range(1, 101):
#     num.append(i)
# print(num)

# num = [i for i in range(1, 101)]
# print(num)

# num = []
# for i in range(0, 101):
#     if i % 2 == 0:
#         num.append(i)
# print(num)

# num = [i for i in range(0, 101) if i % 2 == 0]
# print(num)

# petrol = {
#     'Ai 100' : 60,
#     'Ai 95' : 55,
#     'Ai 92' : 50,
#     'Ai 80' : 40,
#     'DT' : 30
# }
# # new_petrol = { k:v + 10 for k, v in petrol.items() }
# new_petrol = {}
# for key, value in petrol.items():
#     # new_petrol.setdefault(key, value + 10)
#     petrol[key] = value + 10
# print(new_petrol)

# for key, value in petrol.items():
#     if value == 50:
#         petrol[key] = value + 5
# print(petrol)


# lst = [] 
# for i in range(10): 
#     lst.append(i) 
# print(lst)

# lst = [i for i in range(10)]
# print(lst)


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
# new_cars = [x for x in cars if "a" in x]
# print(new_cars)


# squares = [] 
# for i in range(10): 
#     squares.append(i ** 2) 
# print(squares)

# squares = [i ** 2 for i in range(10)] 
# print(squares)

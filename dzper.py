# Строки в python обозначаются кавычками. Приведите все способы.
# Ответ
# str1 = '  '
# str2 = "  "
# str3 = """  """

# Как применяют операции умножения к строкам?
# Ответ
# print(2*"Hello")

# Какие типы данных можно преобразовать в строку?
# Ответ
# integer
# float
# boolean

# Вам дается текст:  -Посчитайте количество букв s и t .
#                    -Найдите все слова, которые начинаются с корня advert (регистр не должен учитываться) и
#                     превратите их все в верхний регистр
tekst = """Advertising companies say advertising is necessary and important.
 It informs people about new products. Advertising hoardings in the street make our environment colourful.
  And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme 
  in the mini-drama.Advertising can educate, too. Adverts tell us about new, healthy products.
    And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. 
    Without advertising, life is boring and colourless.But some consumers argue that advertising is a bad thing.
 They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them.
  Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ 
  to sell their products. Finally, consumers say, if there is advertising there must be rules.
   Some adverts advertise unhealthy things like cigarettes and make people waste their money."""
# print(tekst.count('s'))  #62
# print(tekst.count('t'))  #71
print(tekst.title())
#Списки
# list_1 = [] # Создание пустого списка 
# list_2 = list() # Создание пустого списка 
# list_1 = [7, 9, 11, 13, 15, 17]
#Индексация списков
# list_1 = [7, 9, 11, 13, 15, 17] 
# print(list_1[0]) # 7
#Создание списков через список
# list_1 = list() # создание пустого списка 
# for i in range(5): # цикл выполнится 5 раз
#     n = int(input()) # пользователь вводит целое число
#     list_1.append(n) # сохранение элемента в конец списка
# print(list_1) 
#Длина списка
# list_1 = [7, 9, 11, 13, 15, 17] 
# print(len(list_1)) # 6
# Взаимодействие с циклом for
# list_1 = [12, 7, -1, 21, 0]
# for i in list_1:
#     print(i)
#Индексы
# list_1 = [12, 7, -1, 21, 0]
# for i in range(len(list_1)):
#     print(list_1[i])
#Удаление из списка
# list_1 = [12, 7, -1, 21, 0] 
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21] print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1] print(list_1.pop()) # -1 print(list_1) # [12, 7]
#Добавление элементы
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]
#Срез списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])
# print(list_1[1])
# print(list_1[len(list_1)-1])
# print(list_1[-5])
# print(list_1[:])
# print(list_1[:2])
# print(list_1[len(list_1)-2:])
# print(list_1[2:9])
# print(list_1[6:-18])
# print(list_1[0:len(list_1):6])
# print(list_1[::6])
#Кортежи
# t = () # создание пустого кортежа 
# print(type(t)) # class <'tuple'> t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
#Распаковка кортежей в независимые переменные
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))# r:red g:green b:blue
#Словари
# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'} 
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'} 
# print(dictionary['left']) # ← типы ключей могут отличаться print(dictionary['up']) # ↑ типы ключей могут отличаться dictionary['left'] = '⇐'
# print(dictionary['left'])# ⇐
# print(dictionary['type'])# KeyError: 'type'
# del dictionary['left']# удаление элемента
# Множества
# colors = {'red', 'green', 'blue'} 
# print(colors) # {'red', 'green', 'blue'} colors.add('red')
# print(colors) # {'red', 'green', 'blue'} colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'} colors.remove('red')
# print(colors) # {'green', 'blue','gray'} colors.remove('red') # KeyError: 'red' colors.discard('red') # ok
#Операции со множествами
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}
#Замороженное множество
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})
# List Comprehension
#Простая ситуация — список:
#list_1 = [exp for item in iterable]
#Выборка по заданному условию:
#list_1 = [exp for item in iterable (if conditional)]
#Пример
#Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i) 
#     print(list_1) # [1, 2, 3,..., 100]
# #Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)]# [1, 2, 3,..., 100]
#Пример2
#Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100] Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)] Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0] 
# print(list_1) # [0, 4, 8, 12, 16]          
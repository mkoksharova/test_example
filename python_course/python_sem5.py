# dicti = {"first": 1, "second": 2, "third": 3}

# for keys, value in dicti.items():
#     print(keys, value)
    
# print(dicti.items())

#Вложенные словари
# dict1 = {'Tom': {'English': 5, "Math": 5}, 'Red': {'English': 4, "Math": 4}}

# print(dict1)
# for i in dict1['Tom'].items():
#     print(*i)
# print()
# print(dict1['Red']['Math'])

# dict1.update({'Wer': {'English': 3, "Math": 3}})
# print(dict1)

# dict1['Tom'].update({'Trud': 6})
# print(dict1)

# dict1['Red']['Math'] = 5
# print(dict1)

#Решение задач
#31
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# 0 1 1 2 3 5 8
# Задание необходимо решать через рекурсию
# 1 решение
# n = int(input("Введите число: "))
# def fib(n):
#     if n in [1, 2]: # Условие выхода из рекурсии. Базис
#         return 1
#     return fib(n - 1) + fib(n -2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))

# fib(n)
# print(list_1[n])
# 2 решение
# def f(n):
#     if n == 0 or n == 1:
#         return n
#     return f(n - 1) + f(n - 2)

# print(f(int(input('Введите N-ое число последовательности Фибоначчи: '))))

#33
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#Мое решение
# n = int(input('Введите количество оценок: '))
# grade_list = list()
# for i in range(n):
#     grade = int(input('Введите оценку: '))
#     grade_list.append(grade)
# print(grade_list)

# for j in grade_list:
#     if grade_list[j] >= 4:
#         grade_list[j] = 1
# print(grade_list)

#Решение учителя:
# n = int(input('Введите количество оценок: '))
# grade_list = list()
# for i in range(n):
#     grade = int(input('Введите оценку: '))
#     grade_list.append(grade)
# print(grade_list)

# max_grade = max(grade_list)
# min_grade = min(grade_list)

# for i in range(len(grade_list)):
#     if grade_list[i] == max_grade:
#         grade_list[i] = min_grade
# print(grade_list) 

#35
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def prime(n):
#     i = 2
#     flag = True
#     while i < n and flag:
#         if n % i == 0:
#             flag = False
#         i += 1
#     if flag:
#         return 'yes'
#     return 'no'

# print(prime(int(input(  ))))

# def prime(n):
#     i = 2
#     flag = True
#     while i < n // 2 + 1 and flag:
#         if n % i == 0:
#             flag = False
#         i += 1
#     if flag:
#         return 'yes'
#     return 'no'

# print(prime(int(input(  ))))
        
#37
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# def f(n):
#     if n == 0:
#         return ''
#     x = int(input())
#     return f(n-1) + f' {x}'

# print(f(int(input())))



# 1
# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while

# n = int(input('Введите факториал: '))
# i = 1
# res = 1
# while i <= n:
#     res *= i
#     i += 1
# print(res)
# 2
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи 
# оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

# first_digit = 0
# second_digit = 1
# n = int(input('Введите число: '))
# schet = 1
# while first_digit < n:
#     x = first_digit + second_digit
#     first_digit = second_digit
#     second_digit = x
#     schet +=1
# if first_digit != n:
#     print(-1)
# else:
#     print(schet)
#3 
# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики 
# за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50
# n = int(input('Введите количество дней: '))
# just_count = 0
# max_count = 0
# for i in range(n):
#     temp = int(input('Введите температуру: '))
#     if temp > 0:
#         just_count += 1
#     else:
#         if max_count < just_count:
#             max_count = just_count
#         just_count = 0
# print(max_count)
#4   
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, 
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, 
# а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и 
# самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза
# n = int(input('Введите кол-во арбузов: '))
# max_ar = 0
# min_ar = 10
# for i in range(n):
#     weigth = int(input('Введите вес: '))
#     if weigth >= max_ar:
#         max_ar = weigth
#     if weigth < min_ar:
#         min_ar = weigth
    
        
# print(min_ar, max_ar)
        
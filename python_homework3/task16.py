# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3
# -> 1
n = int(input('Введите количество элементов в массиве: '))
task_list = list()
for _ in range(n):
    k = int(input('Введите элемент массива: '))
    task_list.append(k)

x = int(input('Введите искомое число: '))
count = 0
for j in task_list:
    if x == j:
        count += 1
print(count)



    
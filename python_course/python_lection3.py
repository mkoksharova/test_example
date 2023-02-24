# task 1
# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# n = int(input()) # 5 
# print(sumNumbers(n)) # 15
#1 способ импорта функции (или вызова функции из другого файла)
# import module1
# print(module1.max1(5,9))
#2 способ импорта функции (или вызова функции из другого файла)
# from module1 import max1
# print(max1(10,9))
#3 способ импорта функции (или вызова функции из другого файла) - импортировать все функции
# from module1 import *
#4 способ
# import module1 as m1
# print(m1.max1(10,9))
#Рекурсия
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i - 2))
print(list_1)

#сортировка слиянием
def merge_sort(nums): 
    if len(mid) > 1:
    mid = len(nums) // 2 
    left = nums[:mid] 
    right = nums[mid:] 
    merge_sort(left) 
    merge_sort(right) 
    i=j=k=0
    while i < len(left) and j < len(right): 
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1 
        else:
            nums[k] = right[j]
            j += 1 
        k += 1
    while i < len(left): 
        nums[k] = left[i] 
        i += 1
        k += 1
    while j < len(right): 
        nums[k] = right[j] 
        j += 1
        k += 1
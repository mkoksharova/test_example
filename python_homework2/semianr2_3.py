# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
n = int(input("Введите число n: "))
digit = 2
for i in range(n):
    if digit ** i < n:
        print(digit ** i, end = ' ')
    
#32 Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
list_1 = [10, 20, 40, 100, 90]
min_number = int(input('Введите начало диапозона: '))
max_number = int(input('Введите конец диапозона: '))
final_list = list()
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        final_list.append(i)
print(final_list)
       
# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
n = int(input('Введите количество монеток: '))
count = 0
for i in range(n):
    side = int(input('Введите какой стороной лежит монетка (1 - орел, 0 - решка): '))
    if side == 1:
        count += 1
if count < n / 2:
    print(count)
else:
    print(n - count)


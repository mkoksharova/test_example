# def sum(x, y): 
#     return x + y
# # ⇔ (равносильно)
# sum = lambda x, y: x + y

# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
# data = [1, 2, 3, 5, 8, 15, 23, 38] 
# out = []
# for i in data :
#     if i % 2 == 0: 
#         out.append((i, i ** 2))
# print(out)
#Lamda
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38] 
# res = select(int, data)
# res = where(lambda x: x % 2 == 0, res) 
# print(res) # [2, 8, 38]
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)
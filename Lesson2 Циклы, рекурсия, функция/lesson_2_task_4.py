"""

4. Найти сумму n элементов следующего ряда
чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.

"""

n = int(input('enter quantity: \n'))

e = 1
s = 0
for i in range(n):
    s = s + e
    e = e / (-2)
print(f' your sequence = {s}')


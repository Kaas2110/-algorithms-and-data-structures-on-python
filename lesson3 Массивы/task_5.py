""""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять
сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести
 полученную матрицу.

"""

matrix = [[] for _ in range(4)]

for line in matrix:
    line_sum = 0
    for i in range(4):
        num = int(input('Введите значение: '))
        line.append(num)
        line_sum += num
    line.append(line_sum)

for line in matrix:
    for num in line:
        print(f'\t{num:>5}', end='')
    print()



""" 
Найти максимальный элемент среди минимальных элементов столбцов матрицы.

"""
import random

matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

for i, line in enumerate(matrix):

    if i == 0:                              # Первую строку копируем для сравнения сразу переходим ко второй строке
        min_line = line.copy()
        for item in line:
            print(f'{item:>5}', end='')
        print()
        continue

    for idx, item in enumerate(line):
        if item < min_line[idx]:            # В строках сравниваем каждый элемент с элементом в копии первой строки
            min_line[idx] = item            # меняем по индексу для сохранения порядка
        print(f'{item:>5}', end='')
    print()

print('-' * len(min_line) * 5)

max_min = min_line[0]
for item in min_line:
    print(f'{item:>5}', end='')
    if item > max_min:
        max_min = item

print()
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max_min}')
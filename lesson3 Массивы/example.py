
list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

for i, item in enumerate(list_1):
    del item

print(list_1)

for i, item in enumerate(list_2):
    list_2.remove(item)

print(list_2)

for i, item in enumerate(list_3):
    list_3.pop(i)

print(list_3)

for i, item in enumerate(list_4[:]):
    list_4.remove(item)

"""
крестики-нолики
"""
row = [''] * 3
board = [row] * 3
print(board)
board [1][1] = 'x'
print(board)

board = [[''] * 3 for _ in range(3)]
board[2][2] = 'x'
print(board)


#3 те же операнды, но другая история

a = [1, 2, 3, 4]
b = a

a = a + [5,6,7]
print(a, b)
a = [1, 2, 3, 4]
b = a

a += [5,6,7]
print(a, b)

"""
игла в стоге сена

"""

t = ('one', 'two')
for i in t:
    print(i)

    t = ('one',)
for i in t:
    print(i)



"""

сохраним уникальные значения

"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 2, 3, 4, 5, 6]

lst = list(set(lst))
print(lst)


"""
создадим множество и список
"""

set_x = {1, 2, 3, 4}
lst_x = [10, 20, 30, 40]
# dict_x = {set_x: lst_x}
# dict_x = {lst_x: set_x}
dict_x = {frozenset(set_x): lst_x}
dict_y = {tuple(lst_x): set_x}
print(dict_x, dict_y)

"""

---------------------------------- 2 УРОК
# """
some_string = []
left = 0

right = len(some_string) - 1

pos = len(some_string) // 2

import random

def bin_search(array, value):
    left = 0
    right = len(array) - 1
    pos = len(array) // 2
    while array[pos] != value and left <= right:
        if value > array[pos]:
            left = pos + 1
        else:
            right = pos - 1

        pos = (left + right) // 2

    return -1 if left > right else pos


a = [random.randint(0, 1000) for _ in range(100)]

a.sort()
print(a)

n = int(input('Какой элемент найти'))
print(bin_search(a, n))
"Разложить положительные и отрицательные числа по разным массивам ------------------3"

import random

array = [random.randint(-100, 100 ) for _ in range(100)]

print(array)

arr_below = []
arr_lager = []

for item in array:
    if item > 0:
        arr_lager.append(item)
    elif item < 0:
        arr_below.append(item)

arr_below.sort()
arr_lager.sort()
print(arr_below)
print(arr_lager)


arr_below = [item for item in array if item < 0]
arr_lager = [item for item in array if item > 0]


"""
Вставка элемента в произвольное место массива
"""
import random
array = [random.randint(-100, 100) for _ in range(100)]
print(array)

num = int(input("Введите число для вставки"))

pos = int(input("На каккую позицию вставить число"))
#ДО ЭТОГО МЕСТА, РАЗУМЕЕТСЯ
array.append(None)

i = len(array) - 1
while i > pos:
    array[i], array[i - 1] = array[i -1], array[i]
    i -= 1
array[pos] = num
"""
Все что за коменчено выше входит в одну строку 'array.insert(pos, num)'
"""
array.insert(pos, num)

print(array)


"""
-----------------УРОК 4  

"""
#Генерируем матрицу при помощи генератора списка, вкладываем один генератор в другой и получаем чудо
import random

matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
for line in matrix:
    for item in line:
        print(f'{item:>4}', end = '')
    print()


matrix = [[random.randint(1,20) for _ in range(3)] for _ in range(5)]

for line in matrix:
    for item in line:
        print(f'{item:>4}', end = ' ')
    print()

sum_column = [0] * len(matrix[0])

for line in matrix:
    sum_line = 0

    for i, item in enumerate(line):
        sum_line = sum_line + item
        sum_column[i] = sum_column[i] + item

        print(f'{item:>5}', end = ' ')

    print(f'  | {sum_line}')

print('-' * (len(matrix) * 5))

for s in sum_column:
    print (f'{s:>5}', end = '')





"""
Задача с ассоциативным массивом

"""

# k = int(input('Введите колличество предприятий'))
# enterprises = {}
#
# for i in range(1, k +1):
#     name = input('Введите название предприятия: ')
#     enterprises[name] = [float(input('План')), float(input('Фак: '))]
#     enterprises[name].append(enterprises[name][1] / enterprises[name][0])
#
# print('Факт прибыль больше 10, но план не выполнен (меньше 100%)')
#
# for key, value in enterprises.items():
#     if value[1] > 10 and value[2] < 1:
#         print(f' Предприятие  {key} заработало {value[1]}, что составило {value[2] * 100:2f}%')
#
#
#


#---------------------  1 задача домашки

"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. 
Примечание: 8 разных ответов.
"""
# a = [0] *8
#
# for i in range(2, 100):
#     for j in range(2, 10):
#         if i % j == 0:
#             a[j-2] += 1
#
# for k, l in enumerate(a, start=2):
#     print(f'Числу {k} кратно {l} чисел')


"""
2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив 
 со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 
 (помните, что индексация начинается с нуля), т. к. именно 
 в этих позициях первого массива стоят четные числа.
"""
# from random import randint
#
# SIZE = 10
#
# array = [randint(1, 100) for _ in range(SIZE)]
# print(array)
#
# result = []
#
# for i in range(len(array)):
#     if array[i] % 2 == 0:
#         result.append(i)
#
# print(f'Индекс четных элементов: {result}')


"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""
# import random
#
# SIZE = 10
# array = [random.randint(1, 100,) for _ in range(SIZE)]
# print(array)
# idx_min = 0
# idx_max = 0
#
# for i in range(SIZE):
#     if array[i] < array[idx_min]:
#         idx_min = i
#     elif array[i] > array[idx_max]:
#         idx_max = i
#
# print(f'Min= {array[idx_min]} в ячейке: {idx_min},'
#       f' \nMax= {array[idx_max]} в ячейке: {idx_max}')
# array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
# print(array)
#


"""
4. Определить, какое число в массиве встречается чаще всего.
"""

# import random
#
# SIZE = 10
# array = [random.randint(0,SIZE // 1.5) for _ in range(SIZE)]
# print(array)
#
# num = array[0]
# max_frq = 1
#
# for  i in range(SIZE -1):
#     frq = 1
#
#     for k in range(i + 1, SIZE):
#         if array[i] == array[k]:
#             frq += 1
#     if frq > max_frq:
#         max_frq = frq
#         num = array[i]
#
# if max_frq > 1:
#     print(f'Число {num} встречается {max_frq} раз')
#
# else:
#     print('Все элементы уникальны')
#
# # Можно создать словарь
# diction = {}
#
# for item in array:
#     if item in diction.keys():
#         diction[item] += 1
#     else:
#         diction[item] =1
#
# print(diction)


"""
5. В массиве найти максимальный отрицательный элемент.
 Вывести на экран его значение и позицию в массиве.
"""
# import random
# SIZE = 10
# array = [random.randint(-100, 100,) for _ in range(SIZE)]
# print(array)
#
# i = 0
# index = -1
# while i < SIZE:
#     if array[i] < 0 and index == -1:
#         index = i
#     elif array[i] < 0 and array[i] > array[index]:
#         index = i
#     i += 1
#
# print(f'Число {array[index]} на позиции {index}')

"""
6. В одномерном массиве найти сумму элементов,
 находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
"""
#
# import random
#
# SIZE = 10
# array = [random.randint(-100, 100) for _ in range(SIZE)]
# print(array)
#
# value_min = 0
#
# value_max = 0
#
# for i in range(1, SIZE):
#     if array[i] < array[value_min]:
#         value_min = i
#     elif  array[i] > array[value_max]:
#         value_max = i
# print(array[value_min], array[value_max])
#
# if value_min > value_max:
#     value_min, value_max = value_max, value_min
#
# summ = 0
#
# for i in range(value_min + 1, value_max):
#     summ += array[i]
#
# print(summ)
#



"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
#
# import random
#
# SIZE = 10
# array = [random.randint(-100, 100) for _ in range(SIZE)]
# print(array)
#
# if array[0] > array[1]:
#     min_value_1 = 0
#     min_value_2 = 1
# else:
#     min_value_1 = 1
#     min_value_2 = 0
#
# for i in range(2,SIZE):
#     if array[i] < array[min_value_1]:
#         spam = min_value_1
#         min_value_1 = i
#
#         if array[spam] < array[min_value_2]:
#             min_value_2 = spam
#     elif  array[i] < array[min_value_2]:
#         min_value_2 = i
#
# print(f'Число {array[min_value_1]}, в ячейке min {min_value_1}')
# print(f'Число {array[min_value_2]}, в ячейке min {min_value_2}')
#
#
#

"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. 
Программа должна вычислять сумму введенных элементов каждой строки и
 записывать ее в последнюю ячейку строки. В конце следует вывести 
 полученную матрицу.
"""
# M = 5
# N = 4
# matrix = []
#
# for i in range(N):
#     row = []
#     summ = 0
#
#     for j in range(M-1):
#         num = int(input(f'Строка {i}, элемент {j}: '))
#         summ += num
#         row.append(num)
#
#     row.append(summ)
#     matrix.append(row)
#
# for line in matrix:
#     for item in line:
#         print(f'{item:>4}', end='')
#     print()
#
#


"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
Примечание: попытайтесь решить задания без использования
 функций max, min, sum, sorted 

"""

# import random
# SIZE = 5
# matrix = [[random.randint(1, 100) for _ in range(SIZE)] for _ in range(SIZE)]
#
# for line in matrix:
#     print(*line, sep='\t')
#
# max_ = matrix[0][0]
#
# for j in range(SIZE):
#     min_ = matrix[0][j]
#
#     for i in range(SIZE):            # В этих двух циклах вот что происходит: вначале проверяется самый первый элемент
#                                     # потом мы спускаемя в нижний цикл и пропускаем все первые элементы всех столбоцв
#                                     # и мы их сравниваем - находим наименьший
#         if matrix[i][j] < min_:
#             min_ = matrix[i][j]
#     if min_ > max_:
#         max_ = min_
#
# print(f'Max in min = {max_}')
#
# print(matrix[0][3])


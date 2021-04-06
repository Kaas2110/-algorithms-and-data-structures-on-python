"""
2. Посчитать четные и нечетные цифры введенного
натурального числа. Например, если введено число
34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

"""

numerals = input("Enter any number ")

even = 0

odd = 0

for numeral in numerals:
    if int(numeral) % 2 != 0:
        odd += 1

    else:
        even += 1

print(f'В веденном числе {numerals}, есть {even} четных числа и {odd} нечетных числа')

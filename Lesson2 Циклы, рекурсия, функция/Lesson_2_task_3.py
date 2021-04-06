"""

3. Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486, надо
вывести 6843.

"""

somenumb = int(input('Enter numbers for reverse'))
somenumb_2 = 0

while somenumb > 0:
    digit = somenumb % 10
    somenumb = somenumb // 10
    somenumb_2 = somenumb_2 * 10
    somenumb_2 = somenumb_2 + digit

print(f'its inverse number {somenumb_2}')




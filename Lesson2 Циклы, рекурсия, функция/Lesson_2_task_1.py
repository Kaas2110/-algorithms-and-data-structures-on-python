"""
1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся
пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы
должно    выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'),
программа должна сообщать об ошибке и снова запрашивать знак
операции. Также она должна сообщать пользователю о невозможности
деления на ноль, если он ввел его в качестве делителя.

"""


equation = input('Enter any numbers or enter zero for exit: \n')

while equation != '0':

    eq = list(equation.split())
    a = float(eq[0])
    b = float(eq[2])
    answer = 'Неправильно введен пример'

    if eq[1] == "+":
        answer = a + b
    elif eq[1] == "-":
        answer = a - b
    elif eq[1] == "*":
        answer = a * b
    elif eq[1] == "/":
        if b != 0:
            answer = a / b
        else:
            print('you cannot divide by zero')

    else:
        print('you have problem, enter again')

    print(f'{equation} = {answer}')

    equation = input('Enter any numbers or enter zero for exit: \n')

print("Good buy")







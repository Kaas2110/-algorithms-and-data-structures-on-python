# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple
QUARTERS = 4

Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input("Введите колличество предприятий: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название предприятия {i}: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f"Прибыль за {j + 1}-й квартал:  ")))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)
    all_companies.add(comp)
    total_profit += profit

avarage = total_profit / num
print(f'\nСредняя прибыль = {avarage}')
print(all_companies) # показываю как выглядит множество
print(f'\nПредприятия с прибылью выше среднего: ')
for comp in all_companies:
    if comp.profit > avarage:
        print(f'Компания {comp.name} заработала {comp.profit}')

print(f'\n Предприятия ниже среднего: ')
for comp in all_companies:
    if comp.profit < avarage:
        print(f'Компания {comp.name} заработала {comp.profit}')
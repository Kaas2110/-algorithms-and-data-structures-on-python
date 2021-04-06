"""
Коллекции, модуль Collections
"""
# ЕСТЬ ЕЩЕ Counter Dequ, Defaultdict   - каунтер возращает пару "ключ - значение" в качестве ключа у нас значение,
# в качестве значения - колличество повторений****************
#Дэйкью это очередь, насколько я понял одно из кртуых вещей в нем это возможность при помощи метода leftappend добавлять
# пару вначало словар, также необязательный аргумент этого метода ставит ограничение на колличество пар, которое
# может содержаться в словаре - deque(iteration, maxSize)
# дефолт дикт волшебная поебень, с помощью него можно делать итерацию объекта ( если к дефотдикт прихуярить инт
# defaultdict(int), то его можно проитерировать при помощи for in  с обычным словарем такое не прокатит:
# s = 'dsdafvcxbrfhgassd' \n b = defaultdict(int) \n for i in s: \n b[i] += 1\n print(b), также можно вместо инт
# подставить лист или сет : list_1 = пары ключь - значение \n c = defaultdict \n for k/ v in list_1: \n c[k].append(v)


from collections import OrderedDict  # упорядоченный словарь

a = {'cat': 5, 'mouse': 4, 'dog': 2}
new_a = OrderedDict(sorted(a.items(), key= lambda x: x[0]))    # насколько я понял здесь принцип таков: сортед
                                                             # используется для сортировки, итемс для тоого
# чтобы вернуть пару -ключ-значение, а кей равный функции лямда указывает на x  который вроде как приравнивается
# к индексу при использовании квадратных скобок, вот такой прием не знаю как по-другому объяснить.
print(new_a)

b = {'cat': 5, 'mouse': 4, 'dog': 2}
new_b = OrderedDict(sorted(a.items(), key= lambda x: x[1]))

print(new_b)


new_b.move_to_end('mouse', last= False)
print(new_b)

new_b.popitem(last=False)    # если использовать в попитем фолс, то вместо последнего элемента удаляется первый

print(new_b)

"""
В  log файл сервер добавляет ip- адреса, с которых пришел запрос
Проанализировать последние N адресов и сохранить в новый файл пары значение "ip-адрес - количество запростов"

Исключить локальные ip-адреса: 192.168*
сохранить исходный порядок адресов
"""
#
# from collections import OrderedDict, defaultdict, deque
#
# N = 3000
#
# with open ('какой-то файл', 'r', encoding='utf-8') as f:
#     log = deque(f, N)
#
# print(log)
#
# data = OrderedDict()
#
# spam = defaultdict(int)
#
# for item in log:
#     ip = item[:-1]
#
#     if not ip.startswith('192.168'):
#         spam[ip] += 1   # в этом словаре мы фиксируем сколько раз встречается тоот или иной ключ
#         data[ip] = 1    # здесь нам нужно зафиксировать порядок, чтобы он не прыгал как шлюха
#
# data.update(spam) #  в словарь дата добавляем ключи из словаря спам
#
# print(data)
#
# with open("какой-то другой файл", 'w', encoding='utf-8') as f:
#     for key, values in data.items():
#         f.write(f'{key} - {values}\n')
"""
Namedtuple

"""

from collections import namedtuple

hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)

class Person:
    def __init__(self, name, race, health, mana, strenght):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strenght = strenght

hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)

print(hero_2.mana)


# Пример работы с классом, а теперь приступим в выполнению namedtuple

New_Person = namedtuple('New_Person', 'name, race, health, mana, strenght') # вначале мы передаем наззвание класса
# т.е. то что слева должно ровняться тому что справа,
hero_3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)

print(hero_3.race)

# Вариант работы со списком 
print('*'* 50)
prop = ['name', 'race', 'health', 'mana', 'strenght']
New_Person_1 = namedtuple('New_Person', prop, rename=True) # в именнованный кортэж можно даже в значения добавить
# список, как мы и сделали здесь- добавили prop
hero_4 = New_Person_1('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_4)


""" 
ChainMap - позволяет организовать работу с несколькими словарями (dict)
Поиск ключа осщуествляется последовательно в каждом из словарей цепочки, пока "ключ" не будет найдет
"""
from collections import ChainMap

d_1 = {'a': 2, 'b': 4, 'c': 6}
d_2 = {'a': 10, 'b': 20, 'd': 40}

d_map = ChainMap(d_1, d_2)
print(d_map)

d_2['a'] = 100
print(d_map)
# d_map.new_child({'a': 111, 'b': 222, 'c': 333}) - метод ньючайлд добавляет новый словарь  начало , если он пустой,
# то добавляется пустой словарь


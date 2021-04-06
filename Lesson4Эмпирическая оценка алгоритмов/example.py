# import timeit
#
#
#
# print(timeit.timeit('x = sum(range(0, 10))'))


# import cProfile
#
# def get_len(array):
#     return len(array)
#
# def get_sum(array):
#     s = 0
#     for i in array:
#         s += i
#     return s
#
# def main():
#     lst = [i for i in range(10000000)]
#     a = get_len(lst)
#     b = get_sum(lst)
#
# cProfile.run('main()')
# import cProfile
# def test_fib(func):
#     lst = [0, 1, 1, 2, 3, 5,8 ,13, 21, 34]
#     for i, item in enumerate(lst):
#         assert item == func(i)
#         print (f'Test {i} OK')
#
#
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 1) + fib (n -2)
#
# cProfile.run('fib(15)')
# "example.fib(10)"
# 1000 loops, best of 5: 17.9 usec per loop
# "example.fib(15)"
# # 1000 loops, best of 5: 208 usec per loop
#  1973/1    0.001    0.000    0.001    0.001 example.py:33(fib)


# test_fib(fib)



def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5,8 ,13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print (f'Test {i} OK')


def fib_dict(n):
    fib_d = {0: 0, 1: 1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n - 1) + _fib_dict(n -2)
        return fib_d[n]

    return _fib_dict(n)

# test_fib(fib_dict)


# cProfile.run('fib_dict(100)')
'''
Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии:
an = a1 + (n-1) * d.

Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''

# def seqElemArray(n, d, a):
#     array = [n = (i - 1) * d for i in range(1, n + 1)]    # через listcomprications
#     # array = []
#     # for i in range (1, a + 1):
#     #     array.append(n + d * (i-1))
#     return array

# first_num = int(input('Input fist number: '))
# diff_num = int(input('Input difference number: '))
# amount_elems = int(input('Input number of array elements: '))
# print(seqElemArray(first_num, diff_num, amount_elems))

from random import randint
"эталон)))"
# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
# print(a1 + i * d)

'''
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
в вводе дб диапазон!

Вывод: [1, 9, 13, 14, 19] - тут вывод индексов чисел из списка
'''


def randArray(n):
    array = [randint(-20, 20) for _ in range(n)]
    print(array)
    return array


def indexRangeArray(my_list, min_r, max_r):
    index_list = []
    for i in range(len(my_list)):
        if my_list[i] >= min_r and my_list[i] <= max_r:
            index_list.append(i)
    return index_list


array_size = int(input('Input number array size: '))
# array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
array = randArray(array_size)
min_range = int(input('Input min range number:'))
max_range = int(input('Input max range number:'))
print(indexRangeArray(array, min_range, max_range))


"эталон)))"
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
# if min_number <= list_1[i] <= max_number:
# print(i)

# + вариант
# range_list = [i for i in range(
#     len(num_list)) if num_list[i] >= minimum and num_list[i] <= maximum]

# out_red(range_list)

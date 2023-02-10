'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
'''
# from random import randint

# def randArray(n):
#     array = [randint(-20, 20) for _ in range(n)]
#     print (*array)
#     return array

# set_size1 = int(input('Input fist number array size: '))
# set_size2 = int(input('Input second number array size: '))

# set_nums1 = randArray(set_size1)
# set_nums2 = randArray(set_size2)

# double_nums_set = sorted(list(set(set_nums1) & set(set_nums2)))
# print(*double_nums_set)

# Решение 2

# lst = [input()]
# lst2 = list(map(int, input().split()))
# lst3 = list(map(int, input().split()))
# count = []
# for i in lst2:
#     for j in lst3:
#         if i == j:
#             count.append(i)
# print(*sorted(set(count)))


'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
4 -> 1 2 3 4
9
'''
# Решение 1
# n = int( input( 'n = ' ) )
# lis = list(map(int, input('-> ').split()))
# n = len(lis)
# lis += lis[:2]
# ma = 0
# for i in range(n):
#     ma = max(ma, lis[i] + lis[i+1] + lis[i+2])
# print(ma)

# Решение 2
# bush_amount = int(input('type amount of bushs: ')) # кол-во кустов
# berries_list = [int(input('type amount of berries: ')) for i in range(bush_amount)] # кол-во ягод на 1 кусте на грядке
# res_list = []
# res1 = berries_list[0] + berries_list[-1] + berries_list[-2]
# res_list.append(res1)
# res2 = berries_list[0] + berries_list[1] + berries_list[-1]
# res_list.append(res2)
# for berries in range(2, len(berries_list)):
#     res = berries_list[berries] + berries_list[berries - 1] + berries_list[berries - 2]
#     res_list.append(res)
# print(max(res_list))


                
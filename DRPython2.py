'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 0 1 1 1 0
2
'''
# import random

# def inputCoinsNum(n):
#     while n <= 0:
#         n = int(input('Please input a positive number of coins: '))
#     return (n)

# def coinsToSide(n):
#     sum_0side = 0
#     sum_1side = 0

#     for i in range(1, n + 1):
#         side = random.randint(0,1)
#         print(f'#{i} coin is "{side}" side ')
#         if side == 0:
#             sum_0side += 1
#         else:
#             sum_1side += 1
#     return(sum_0side, sum_1side)

# def minFlipSide(n, m):
#     print(f'|{n} coins "0" side| {m} coins "1" side|')
#     print()

#     if n == 0 or m == 0:
#         if m == 0:
#            print(f'All {n} coins are on side "0"')
#         else:
#            print(f'All {m} coins are on side "1"')
#     elif n < m:
#         print(f'You need to flip {n} coins with side "0"')
#     elif n > m:
#         print(f'You need to flip {m} coins with side "1"')
#     else:
#         print(f'You need to flip {n} coins with any side "0" or "1"')


# n = int(input('Input number of coins: '))
# (sum_0, sum_1) = coinsToSide(inputCoinsNum(n))
# minFlipSide(sum_0, sum_1)


'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
'''
# s = 5
# p = 6

# def twoNumbersOutput(s, p):
#     for x in range(1, 1001):
#         y = s - x
#         if x <= y and x * y == p:
#             print()
#             print(f'Sum {s} and product {p} of numbers -> {x} and {y}')
#             print(s, p, '->', x, y)

# sum_numbers = int(input('Input the sum of two numbers(X,Y≤1000): '))
# prod_numbers = int(input('Input product of two numbers(X,Y≤1000): '))

# twoNumbersOutput(sum_numbers, prod_numbers)

# Решение 2
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)


'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N.
10 -> 1 2 4 8
'''
# def CorrectInpNum(n):
#     while n <= 0:
#         n = int(input('Please input a positive number: '))
#     return (n)

# def Degree2num(n):
#     degTable = list()
#     for i in range(n):
#         k = 2**i
#         if k <= n:
#             degTable.append(k)
#     print(f'{n} -> {degTable}')

# number = int(input('Input number: '))
# Degree2num(CorrectInpNum(number))

# Рещение 2
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

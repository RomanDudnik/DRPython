'''
Задача 2: Найдите сумму цифр трехзначного числа. 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''
# number = int(input('Input a three-digit number: '))

# def sumThreeDig(n):
#     sum = n // 100 + n % 10 + (n % 100)//10
#     return(sum)
    
# result = sumThreeDig(number)
# print(f"The sum of the digits of {number} is  {result}")

'''
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
'''

# s = int(input('Input total number of crafts: '))
# # ser = x
# # pet = x
# # kat = (x + x)*2
# # s = x + x + (x + x)*2
# # s = 6x
# ser = int(s/6)
# pet = int(ser)
# kat = int((ser + pet)*2)

# print (f"Out of {s} crafts, Petya and Seryozha made {ser} each, and Katya made, {kat} crafts")
# print (s,'=>',ser, '|' ,kat, '|' ,pet)

'''
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
'''

# number = int(input('Input your six-digit ticket number: '))

# left_num = number // 1000
# right_num = number % 1000

# def sumThreeDig(n):
#     sum = n // 100 + n % 10 + (n % 100)//10
#     return(sum)

# if (sumThreeDig(left_num) != sumThreeDig(right_num)):
#     print(f"Your ticket {number} is not lucky :( ")
# else:
#     print(f"Your ticket {number} turned out to be Lucky!!! ")

'''
# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
'''

# n = int(input('Input the number of the first row: '))
# m = int(input('Input the number of the second row: '))
# k = int(input('Input the required number of sections: '))

# if n == k or m == k and n > 1 and m > 1:
#     print(f"You will manage to get {k} sections with one rift (YES)")
# elif n == k or m == k and n >= 1 and m >= 1:
#     print(f"You will get your {k} sections without breaking (NO)")
# else:
#     print(f"Can't get {k} sections with a single rift (NO)")

'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
'''
# day = int(input("Введите номер дня недели: "))

# def weekend(d):
#     if d > 0 and d < 8:
#         if d < 6:
#             print (f'День {d} - рабочий день :(NO)')
#         else:
#             print (f'День {d} Выходной!!!(YES)')
#     else:
#         print (f"Вы ввели не день недели, попробуйте числа от 1 до 7!")
# weekend(day)

'''
Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
в которой находится эта точка (или на какой оси она находится).
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''

x = int(input('Enter the x-coordinate: '))
y = int(input('Enter a y-coordinate: '))

def quarter(x, y):
    if x > 0 and y > 0:
        print("This point on 1st quater")
    elif x < 0 and y > 0:
        print("This point on 2st quater")
    elif x < 0 and y < 0:
        print("This point on 3st quater")
    elif x > 0 and y < 0:
        print("This point on 4st quater")
    else:
        print("Its imposible at this task!")

quarter(x, y)


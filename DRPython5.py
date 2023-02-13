'''
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''

# def exponent(a,b):
#     if (b == 0):
#         a = 1
#         return a
#     elif b == 1 :
#         return a
#     return a * exponent(a, b-1)
    

# num = int(input('Input your number: '))
# exp = int(input('Input exp number: '))
# print(f'{num} to the power of {exp} will be -> {exponent(num,exp)}')


'''
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4
'''
# Решение по условию задачи:
    
# def sumNum(a, b):
#     if a == 0 or b == 0:
#         if a > b:
#             return a
#         return b
#     elif (b == 1):
#         return a + 1
#     return sumNum(a+1, b-1)
        
# num_1 = int(input('Input first Positive! number: '))  
# num_2 = int(input('Input second Positive! number: '))
# print(f'{num_1} + {num_2} = {sumNum(num_1, num_2)}')

# Решение задачи для любых целых чисел:

def sumNum(a, b):
    if a == 0 or b == 0:
        if a > b:
            return a
        return b
    
    elif b < 0:
        if (b == -1):
                return a - 1
        return sumNum(a - 1, b + 1)    
        
    elif (b == 1):
        return a + 1
    return sumNum(a + 1, b - 1)
        
num_1 = int(input('Input first number: '))  
num_2 = int(input('Input second number: '))
print(f'{num_1} + {num_2} = {sumNum(num_1, num_2)}')
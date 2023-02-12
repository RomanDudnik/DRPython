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

# def doubleNumsSet(set1, set2):
#     a = sorted(list(set(set1) & set(set2)))
#     if a == []:
#         print('No double numbers')
#     print(*a)


# set_size1 = int(input('Input fist number array size: '))
# set_size2 = int(input('Input second number array size: '))

# doubleNumsSet(randArray(set_size1), randArray(set_size2))


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

from random import randint

def randArray(n):
    array = [randint(1, 10) for _ in range(n)]
    print (*array)
    return array

def max3elemSum(array):
    n = len(array)
    array += array[:2]
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, array[i] + array[i+1] + array[i+2])
    return max_sum

n = int( input( 'Input the number of bushes on row: ' ) )
print(f'-> {max3elemSum(randArray(n))}')



                
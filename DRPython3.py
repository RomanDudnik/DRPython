'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
'''
# from random import randint

# num = int(input('Input number array size: '))
# array = [randint(-10, 10) for _ in range(1, num+1)]
# print (array)

# x = int(input('Input any number: '))

# count_num = array.count(x)

# print (f'-> {count_num}')

'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
'''
from random import randint

def searchCloseNum(array):
    array.append(x)
    print(array)
    array.sort()
    print(array)
    
    if x == array[0]:
        print(array[1])
    elif x == array[-1]:
        print(array[-2])
    else:
        index_x = array.index(x)
        i0 = index_x - 1
        i1 = index_x + 1
        if x - array[i0] < array[i1] - x:
            print(array[i0])
        elif x - array[i0] > array[i1] - x:
            print(array[i1])
        else:
            print(array[i0], array[i1])


num = int(input('Input number array size: '))
new_list = [randint(-10, 10) for _ in range(1, num+1)]
print (new_list)
x = int(input('Input a number to search in the array: '))
searchCloseNum(new_list)

'''
Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод:
12
'''



# def calculate_word_value(word):
#     score = {
#             'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#             'D': 2, 'G': 2,'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#             'B': 3, 'C': 3, 'M': 3, 'P': 3,'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#             'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,'Й': 4, 'Ы': 4,
#             'K': 5,'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#             'J': 8, 'X': 8,'Ш': 8, 'Э': 8, 'Ю': 8,
#             'Q': 10, 'Z': 10,'Ф': 10, 'Щ': 10, 'Ъ': 10
#         }
#     return sum([score[c.upper()] for c in word])

# word = input("Введите слово на русском или английском языке: ")
# value = calculate_word_value(word)
# print("Стоимость слова:", value)


# score = 0
# for i in word:
#     for j in scores.keys():
#         if i in scores[j]:
#             score+=j
#             break


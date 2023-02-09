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

# array_size = int(input('Input number array size: '))
# array = [randint(-10, 10) for _ in range(1, array_size+1)]
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
# from random import randint

# def searchCloseNum(array, x):
#     array.append(x)
#     array.sort()
    
#     if x == array[0]:
#         print(array[1])
#     elif x == array[-1]:
#         print(array[-2])
#     else:
#         index_x = array.index(x)
#         i0 = index_x - 1
#         i1 = index_x + 1
#         if x - array[i0] < array[i1] - x:
#             print(array[i0])
#         elif x - array[i0] > array[i1] - x:
#             print(array[i1])
#         else:
#             print(array[i0], array[i1])


# size_array = int(input('Input number array size: '))
# new_list = [randint(-10, 10) for _ in range(1, size_array+1)]
# print (new_list)
# num = int(input('Input a number to search in the array: '))
# searchCloseNum(new_list, num)

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

# def scrabblePoints(word):
#     alphabet_score = {
#                 1: ('A' , 'E' , 'I' , 'O' , 'U' , 'L' , 'N' , 'S' , 'T' , 'R' ,'А' , 'В' , 'Е' , 'И' , 'Н' , 'О' , 'Р' , 'С' , 'Т') ,
#                 2: ('D' , 'G' ,'Д' , 'К' , 'Л' , 'М' , 'П' , 'У') ,
#                 3: ('B' , 'C' , 'M' , 'P' ,'Б' , 'Г' , 'Ё' , 'Ь' , 'Я') ,
#                 4: ('F' , 'H' , 'V' , 'W' , 'Y' ,'Й' , 'Ы') ,
#                 5: ('K' ,'Ж' , 'З' , 'Х' , 'Ц' , 'Ч') ,
#                 8: ('J' , 'X' ,'Ш' , 'Э' , 'Ю') ,
#                 9: ('Q' , 'Z' ,'Ф' , 'Щ' , 'Ъ') 
#                 }
#     scores = 0
#     for letter in word:
#         for k,v in alphabet_score.items():
#             if letter in v:
#                 scores += k
#                 break
#     return scores    
        
# my_word = input('Input your word: ').upper()
# print(f'word {my_word} is worth {scrabblePoints(my_word)} points')
# # print(f'{my_word} -> {scrabblePoints(my_word)}')
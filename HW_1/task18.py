# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X.
# Если таких элементов несколько, вы вывести один любой.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
# Последняя строка содержит число X
# *Пример:*
# 5
#    7 -2 3 5 1
#    6
#    -> 7
from random import randint
N = int(input('Введите число элементов списка: '))
lst = [randint(1, 20) for i in range(N)]
print(lst)
n = int(input('Введите число х: '))
index_element = 0
min_element = abs(n - lst[0])
for i in range(1, N):
    hear_element = abs(n - lst[i])
    if hear_element < min_element:
        min_element = hear_element
        index_element = i
print(f"Самый близкий по величине элемент к заданному это число {lst[index_element]}")
# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
num = int(input('Введите трехзначное число: '))
if num > 99 and num < 1000:
    n1 = num // 100
    n2 = num // 10 % 10
    n3 = num % 10
    sum = n1 + n2 + n3
    print(f"Сумма цифр числа {num} равна {sum}")
elif num < 0:
    print('Вы ввели отрицательное число ')   
else:
    print('Вы ввели не трехзначное число ')
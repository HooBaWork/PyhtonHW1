##Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X.

from random import randint

N = int(input("Введите число от 1 до 9: "))
if N <= 0 or N > 9:
    print("Вы ввели неверное число.") 
else:
    A = [randint(-9, 9) for i in range(N)]
    print(A)
X = int(input("Введите искомое число: "))

count = 0
for i in A:
    if i == X:
        count += 1
print("Число ", X, "встречается в массиве", count, "раз.")
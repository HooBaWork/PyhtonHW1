# Задача 2: Найдите сумму цифр трехзначного числа.
number = int(input("Введите число: "))
summ = 0
while number > 0:
    summ += number % 10
    number //= 10
print(summ)
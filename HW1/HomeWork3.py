# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

number = input('Введите номер билета')
res = list(map(int, number))
result1 = int(res[0]) + int(res[1]) + int(res[2])
result2 = int(res[3]) + int(res[4]) + int(res[5])
if result1 == result2:
    print('У вас счастливый билет')
else:
    print('Несчастливый билет')

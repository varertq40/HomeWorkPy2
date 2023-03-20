# 2.3[14]: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2^k), не превосходящие числа N.
# Примеры/Тесты:
# 10 ->
# 1
# 2
# 4
# 8

N = int(input("Введите число: "))
powers_two = 1
while powers_two < N:
    print(powers_two)
    powers_two = powers_two * 2
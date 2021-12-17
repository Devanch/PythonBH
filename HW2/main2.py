import math
# a = input()
# b = input()

str_a_b = '3 2 3 4 5 2 4 5'

spis_a = str_a.split(' ')
spis_b = str_b.split(' ')
for i in range(len(spis_a)):
        a = int(spis_a[i])
        b = int(spis_b[i])
        c = math.sqrt(a**2 + b**2)
        S = a*b / 2
        print(f"Треугольник {i} с катетами {a} и {b} имеет площадь {S} и гипотенузу {c}")

import math
# a = input()
# b = input()

str_a = "3 2 3 4"
str_b = "5 2 4 5"

list_a = list(str_a)
list_b = list(str_b)
cnt = list_a.count
for i in range(len(list_a)):
    if (list_a[i] != ' '):
        a = int(list_a[i])
        b = int(list_b[i])
        c = math.sqrt(a**2 + b**2)
        S = a*b / 2
        print(f"Треугольник {i} с катетами {a} и {b} имеет площадь {S} и гипотенузу {c}")



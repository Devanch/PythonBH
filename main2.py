# Получение чисел
# a = float(input()); 
# b = float(input()); 
# c = float(input()); 

# Тестовые данные
a = 3;
b = 2;
c = 1;
print(f"Вы Ввели следующие числа: {a},{b},{c} ")

# Применение формулы
f = float(a**2 + b**2);
g = float(3*b - 4);
h = float(4 * c**5 / 6);

res = f / g ;
resa = res  /  h;

# Вывод результатов
print(resa);

print("Целая часть " + str(res  //  h))
print("Остаток " + str(res  %  h))
print("res: " + str(res))
print("h: " + str(h))

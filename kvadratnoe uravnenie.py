import math
a = int(input("введите число a "))
b = int(input("введите число b "))
c = int(input("введите число с "))
d = b**2 - 4 * a * c
if d < 0:
    print("корней нет")
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print(x1, x2)

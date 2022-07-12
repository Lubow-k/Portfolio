print('Введите три цифры - стороны треугольника')
a, b, c = int(input()), int(input()), int(input())
a1 = max(a, b, c)
c1 = min(a, b, c)
b1 = a + b + c - a1 - c1
d = a1**2 - b1**2 - c1**2
if d == 0: 
    print('Треугольник прямоугольный!')
else:
    print('Треугольник не является прямоугольным')
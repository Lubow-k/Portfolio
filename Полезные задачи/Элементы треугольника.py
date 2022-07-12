#Дан треугольник ABC на плоскости, заданный координатами своих вершин. 
#Для этого треугольника вычислить:
#радиус вписанной в треугольник окружности;
#радиус описанной вокруг треугольника окружности;
#сумму длин трех медиан треугольника.

from math import sqrt

def compute_len(x_0,y_0,x_1,y_1):
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line

def compute_rin(a_1, a_2, a_3):
    p = (a_1 + a_2 + a_3) / 2
    rin = sqrt((p - a_1) * (p - a_2) * (p - a_3)/p)
    return rin

def compute_rout(a_1, a_2, a_3):
    p = (a_1 + a_2 + a_3) / 2
    s = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    rout = (a_1*a_2*a_3) / (4*s)
    return rout

def compute_med (a_1, a_2, a_3):
    med = 1/2 * sqrt(2*(a_1**2 + a_2**2) - a_3**2)
    return med
 
x_a = float(input())
y_a = float(input())

x_b = float(input())
y_b = float(input())

x_c = float(input())
y_c = float(input())

c = compute_len(x_a, y_a, x_b, y_b)

a = compute_len(x_b, y_b, x_c, y_c)

b = compute_len(x_a, y_a, x_c, y_c)

if a + b <= c or b + c <= a or a +c <= b:
    print("error")
    
else:     
    r = round(compute_rin(a,b,c), 4)
    
    R = round(compute_rout(a,b,c), 4)
    
    m1 = compute_med(a,b,c)
    
    m2 = compute_med(a,c,b)

    m3 = compute_med(c,b,a)
    
    M = m1 + m2 + m3
    M = round(M,4)
    print(r, R, M)
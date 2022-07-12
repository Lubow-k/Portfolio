#Доход банка при аннуитетном и дифференцированном расчётах
def pd(t):
    w = s / n + (s - (t - 1) * s / n) * k / 1200
    return w

def pa():
    ka = k / 1200
    pa = (ka * (1 + ka) ** n) / ((1 + ka) ** n - 1) * s
    return pa

s = int(input("Сумма кредита: "))
n = int(input("Срок кредита в месяцах: "))
k = int(input("Процент по кредиту: "))
print()
e = 0

for i in range(1, n + 1):
    print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (i, pd(i), pa()))
    e = e + pd(i)
r = pa() * n 

print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % (e - s, r - s))
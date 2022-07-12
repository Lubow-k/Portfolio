def f(n):
    if n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        k = 5
        r = round(n**0.5)
        while k <= r:
            if n % k == 0:
                return False
            elif n % (k+2) == 0:
                return False
            k += 6
        return True
            
s = 2  
for i in range(3, 2*10**6, 2):
    if f(i):
        s += i

print("Сумма простых чисел до 2000000 равна", s)
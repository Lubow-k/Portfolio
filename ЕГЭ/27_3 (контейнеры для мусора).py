with open("Data_27_3.txt", 'r') as f:
    n = int(f.readline())
    a = []
    for _ in range(n):
        a.append(int(f.readline()))
ans, l, r = 0, 0, 0
for i in range(1, n//2):
    ans += (a[i]*i + a[len(a)-i]*i)
    r += a[i]
    l += a[len(a) - i]
l += a[0]
ans += a[n//2]*(n//2)
ans = [ans] + [0]*(n-1)
for i in range(1, n):
    x = a[(i + n//2 - 1) % n] #старыйсредний
    ans[i] = ans[i-1] + l - r - x
    l = l - a[(i + n//2) % n] + a[i]
    r = r - a[i] + a[(i + n//2 - 1) % n]
print(min(ans) * 3)
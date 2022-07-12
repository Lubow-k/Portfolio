f = open("Data_27_2.txt", "r")
n = int(f.readline())
a = [10**9 for _ in range(30)]
k = s = ms = 0
for _ in range(n):
    b = int(f.readline())
    s += b
    if (b % 2 == 0) and (b > 0):
        k += 1
    d = k % 30
    if d == 0:
        ms = max(ms, s)
    a[d] = min(a[d], s)
    ms = max(ms, s - a[d])
print(ms)
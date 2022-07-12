f = open("Data_27_1.txt")
n = int(f.readline())
r = {0: (0, 0)}
m = 100000000
ms = 0
k = 89
for _ in range(n):
    b = int(f.readline())
    t = {}
    for key in r:
        t[(key + b)%k] = (r[key][0] + b, r[key][1] + 1)
    if b % k not in t:
        t[b % k] = (b, 1)
    r = t.copy()
    if 0 in r:
        if r[0][0] > ms:
            ms = r[0][0]
            m = r[0][1]
        elif r[0][0] == ms:
            m = min(r[0][1], m)
print(m)
with open("Data_26_2.txt", 'r') as f:
    n = int(f.readline())
    d = {}
    for i in range(n):
        line = f.readline().split()
        r, m = int(line[0]), int(line[1])
        if r in d:
            d[r].append(m)
        else:
            d[r] = [m]
m_r = 0
m_m = 0
for c in d:
    r = d[c]
    r.sort()
    for t in range(len(r) - 1):
        if r[t + 1] - r[t] == 14:
            if c > m_r:
                m_r = c
                m_m = r[t] + 1
print(m_r, m_m)
with open('Data_26_1.txt', 'r') as f:
    n = int(f.readline())
    p = []
    for _ in range(604800):
        p.append(0)
    start_pr = 1634515200
    end_pr = 1634515200 + 604800
    c = 0
    for i in range(n):
        line = f.readline().split()
        start = int(line[0])
        end = int(line[1])
        if start < start_pr and (end > start_pr or end == 0):
            c += 1
        if (start >= start_pr) and (start <= end_pr):
            p[start - 1634515200] += 1
    
        if start_pr <= end <= end_pr:
            p[end - 1634515200] -= 1        
ma = 0
ma_k = 1
k = 1
for i in range(604800):
    c += p[i]
    if c == ma:
        k += 1
    if c > ma:
        ma = c
        k = 1
print(ma, k)    
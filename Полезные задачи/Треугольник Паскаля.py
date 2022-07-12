def F(n, k):
    a = []
    j = 1
    for i in range(n):
        a.append([0] * j)
        j += 1

    for i in range(n):
        a[i][0] = 1
        a[i][i] = 1
        for j in range(1, i):
            a[i][j] = a[i-1][j] + a[i-1][j-1]

    for c in a:
        print(*c)

    return(a[n-1][k-1])
    
print(F(10, 2))
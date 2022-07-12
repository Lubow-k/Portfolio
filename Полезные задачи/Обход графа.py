def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not (start in graph):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

'''
Sample Input:
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
'''

n = int(input())
d = {}
for _ in range(n):
    l = input()
    k = l[0]
    l = l[4:].split()
    for c in l:
        if c in d:
            d[c].append(k)
        else:
            d[c] = [k]
print()
print(d)

g = int(input())
for _ in range(g):
    t = input()
    r1 = t[0]
    r2 = t[2]
    if find_path(d, r1, r2) and (r1 in d):
        print("Yes")
    else:
        print("No")
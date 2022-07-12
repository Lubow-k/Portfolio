def max_sum(array):
    m = ending = array[0]
    for i in range(1, len(array)):
        ending += array[i]
        if ending < array[i]:
            ending = array[i]
        m = max(m, ending)
    return m

#Ввод 10 чисел
a = []
for _ in range(10):
    a.append(int(input()))
print(max_sum(a))

#Пример
print(max_sum([-9, 1, 3, 4, -1, 2, 7, -5, 3]))
# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

d = {(0, 0): 0}
def f(n, m):
    if n == 0 or m == 0:
        return 1
    else:
        if (n, m) in d:
            return d[(n, m)]
        else: 
            d[(n, m)] = f(n-1, m) + f(n, m-1)
    return f(n, m)
       
print(f(20, 20))
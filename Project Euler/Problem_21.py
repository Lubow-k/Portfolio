# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
def sum_divisors(n):
    s = 1
    if int(n**0.5) * int(n**0.5) == n:
        s += int(n**0.5)
    if n % 2 !=0:
        for i in range(3, int(n**0.5), 2):
            if n % i == 0:
                s += (i + n // i)
    else:
        for i in range(2, int(n ** 0.5)):
            if n % i == 0:
                s += (i + n // i)
    return s

am_sum = 0
for b in range(2, 10001):
    a = sum_divisors(b)
    if (sum_divisors(a) == b) and (a != b) and b < a:
        am_sum += (a + b)
print(am_sum)
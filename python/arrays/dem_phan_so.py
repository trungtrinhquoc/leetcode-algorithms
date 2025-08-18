
import math

def count_fraction(n):
    fraction = set()
    for i in range(2, n + 1):
        for j in range(1, i):
            if math.gcd(j, i) == 1:
                fraction.add((j, i))
    return len(fraction)

n = int(input())
print(count_fraction(n))
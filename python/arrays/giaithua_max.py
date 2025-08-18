
import math

def count_number_giaithua(n):
    if n == 0 and n == 1:
        return 0
    sum = 0
    for i in range(2, n+1):
        sum += math.log10(i)

    return math.floor(sum) + 1

n = int(input())
print(count_number_giaithua(n))
    
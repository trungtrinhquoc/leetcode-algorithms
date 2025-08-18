n = int(input())
numbers = list(map(int, input().split()))

matrix = []
for i in range(n):
    row = numbers[i * n : (i + 1) * n]
    matrix.append(row)

min_number = float('inf')
for i in range(n):

    min_number = min(min_number, matrix[i][i], matrix[i][n - 1 - i])

print(min_number)
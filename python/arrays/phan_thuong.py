def phanthuong(base, exp, mod):
    result = 1
    base %= mod

    while(exp > 0):
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2

    return result

n = int(input())

exp = n * n
mod = 1000
power_mod = phanthuong(2, exp, mod)

result = (power_mod - 1) % mod

print(result)

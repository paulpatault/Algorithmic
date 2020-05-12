def fast_pow(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        return fast_pow(x * x, n / 2)
    return x * fast_pow(x * x, (n - 1) / 2)


print(fast_pow(2, 10))
print(fast_pow(4, 4))

num = int(2e+6)


def sum_primes(val: int):
    summ: int = 0
    sieve: list = [True] * val
    for i in range(2, val):
        if sieve[i]:
            summ += i
            for j in range(i**2, val, i):
                sieve[j] = False
    return summ


print(sum_primes(num))

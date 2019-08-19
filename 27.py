# This algorithm is written in Python 3.7
import sympy  # I used this library for the function isprime(x) which gives True if x is prime
a_max = 1000
b_max = 1000
primes_amount = -1
found_a = None
found_b = None


for a in range(-a_max+1, a_max):
    for b in range(-b_max, b_max+1):
        eq_prime = True
        n = -1
        while eq_prime:
            n += 1
            eq = n**2 + a * n + b
            eq_prime = sympy.isprime(eq)
        if primes_amount < n - 1:
            primes_amount = n - 1
            found_a = a
            found_b = b
sign = lambda x: ('+', '-')[x < 0]
print("n^2 {} {} * n {} {} ".format(sign(found_a), abs(found_a), sign(found_b), abs(found_b)))
print("The product a * b =", found_a * found_b)
print("0 <= n <=", primes_amount)


# This program is written in Python 3.7
import sympy
prime = 2
counter = 0
maximum = int(1e+6)
while prime < maximum:
    prime_s = str(prime)
    flag = True
    for runner in range(1, len(prime_s)):
        prime_s = prime_s[1:] + prime_s[0]
        flag = sympy.isprime(int(prime_s))
        if not flag:
            break
    counter += flag
    prime = sympy.nextprime(prime)
print(counter)

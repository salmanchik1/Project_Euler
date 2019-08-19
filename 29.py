# This program is written in Python 3.7
from math import sqrt
n = 100
final_list = list()
primes = [x + 2 for x in range(n - 1)]
powers = [1 for x in range(n-1)]

for a in range(int(sqrt(n)) + 1, 1, -1):
    # Calculate the prime divisor for all values of a, put these values into primes list
    # Calculate the powers of prime divisor for all values of a
    b = 2
    while a**b <= n:
        primes[a ** b - 2] = a
        powers[a ** b - 2] = b
        b += 1

for a in range(2, n + 1):
    # Calculate the stings using the prime divisor value for all values of a
    # and if received string is not in the final list add it into the list.
    for b in range(2, n + 1):
        string = str(primes[a - 2]) + "^" + str(b * powers[a - 2])
        if string not in final_list:
            final_list.append(string)

print(len(final_list))

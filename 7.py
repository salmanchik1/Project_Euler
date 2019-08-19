# This program is written in Python 3.7
n = 0
primes = list()
num = 10001


def check(val):
    """Checks whether the value is prime"""
    flag = False
    for j in primes:
        if val % j == 0:
            flag = True
            break
    if not flag:
        primes.append(val)
    return None


i = 5
while len(primes) < num:
    check(i)
    check(i+2)
    i += 6
    # we use the rule that all the primes larger than 3
    # are following these equations: prime[a] = n*6+1 or n*6-1

print("The prime number in #{} position is {}".format(num, primes[num-1]))

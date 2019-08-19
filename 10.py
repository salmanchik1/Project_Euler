from math import sqrt
n = 100
primes = [2, 3]
i = 5
summ = 5


def check(val):
    global summ
    flag = False
    max_j = round(sqrt(val))  # find the square root of the value
    for j in primes[2:]:
        if j > max_j:  # b cannot be larger than the square root of the value
            break
        if val % j == 0:
            flag = True
            break
    if not flag:
        primes.append(val)
        summ += val


while i < n:
    check(i)
    if i + 2 < n:
        check(i + 2)
    i += 6
# print(primes)
print("The sum is:", summ)

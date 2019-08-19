# This program is written in Python 3.7
from math import sqrt


def check(val):
    s = 0
    for i in range(2, int(sqrt(val)) + 1):
        if val % i == 0:
            s += i + val // i
    s += 1
    return s


summ = 0
n = 10000

amiables = list()

for i in range(1, n+1):
    if i in amiables:
        continue
    temp = check(i)
    if temp < n and temp != i and check(temp) == i:
        summ += i + temp
        amiables.append(i)
        amiables.append(temp)
print(summ)

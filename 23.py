# This program is written in Python 3.7
from math import sqrt

def sum_divs(val):
    s = 0
    for i in range(2, int(sqrt(val)) + 1):
        if val % i == 0:
            s += i
            if val != i**2:
                s += val // i
    s += 1
    return s


abundants = list()
for i in range(1, 28123):
    if i < sum_divs(i):
        abundants.append(i)

sums_abundants = [False] * 28124
for i in range(len(abundants)):
    for y in abundants[i:]:
        temp = abundants[i]+y
        if temp > 28123:
            break
        sums_abundants[temp] = True

summ = 0
for i in range(len(sums_abundants)):
    if not sums_abundants[i]:
        summ += i
print(summ)

# This algorithm is written in Python 3.7
n = 1001
summ = 1

for i in range(1, n // 2 + 1):
    summ += 4 * (2*i - 1)**2 + 20 * i

print(summ)

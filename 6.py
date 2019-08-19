# This program is written in Python 3.7
sum1 = 0
sum2 = 0
n = 100
for i in range(1, n+1):
    sum1 += i ** 2
    sum2 += i

sum2 *= sum2
print("The difference between the square of the sum and the sum of squares"
      "for the numbers from 1 to {} is {}".format(n, int(sum2 - sum1)))

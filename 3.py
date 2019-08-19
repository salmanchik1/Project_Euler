# My program made in Python 3.7

number = 600851475143
i = 2
while number > 1:
    if number % i == 0:
        number = int(number/i)
    i += 1
else:
    print('The largest prime factor is: %i' % (i-1))

# My program made in Python 3.7
a, b = 1, 2
maximum = 4e+6
summ = 0
while b < maximum:
    summ += b
    a, b = a + 2*b, 2*a + 3*b
print("The sum of the even-valued terms is: %i" % summ)

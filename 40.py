# This program is written in Python 3.7
import numpy
# I used this library for calculation the product of the list items


def find_digit(number):
    """This function converts the number
    into the digit taken from the sequence of all the numbers written without
    any spaces between them. The sequence begins from 0 and goes to eternity."""
    i = 0
    number1 = number
    # Next loop consequently subtracts the amount of the numbers with exact length
    # while it is possible
    while number1 > 9 * 10**i * (i + 1):
        number1 -= 9 * 10**i * (i + 1)
        i += 1
    # after that we find the number that we use to define the resulting digit
    ord_num = 10**i + (number1-1) // (i + 1)
    # And finally we return that digit
    return int(str(ord_num)[number1 % (i + 1) - 1])


# Calculate the product of all the digits described in the problem
print(numpy.prod([find_digit(10**i) for i in range(7)]))

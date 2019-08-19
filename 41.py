# This algorithm is written in Python 3.7
import sympy


def prev_pandigital(value):
    """This function finds the previous pandigital number"""
    s_value = str(value)
    for i in range(len(s_value)-2, -1, -1):
        # Here we find the first from the end i-th digit
        # larger than next digit in the string.
        if int(s_value[i+1]) < int(s_value[i]):
            # max_digit is the maximal digit which less than i-th digit
            # and has larger index in the string
            max_digit = str(max([int(x) for x in s_value[i+1:] if int(x) < int(s_value[i])]))
            # here we calculate the ending for result
            ending = s_value[i:]
            # find the index of max_digit in the ending
            item_index = ending.find(max_digit)
            # delete the max_digit from the ending
            ending = ending[:item_index] + ending[item_index + 1:]
            # sort the ending in reversed sequence
            return int(s_value[:i] + max_digit + ''.join(sorted(ending, reverse=True)))
    # If we couldn't find the primes with the current length change the length to smaller one
    return sum([(i+1)*10**i for i in range(len(s_value)-1)])


# define the maximal possible pandigital
maximal_pandigital = sum([(i+1)*10**i for i in range(9)])
a = maximal_pandigital
# Run the next loop before we find the prime between pandigitals
while not sympy.isprime(a):
    a = prev_pandigital(a)
print("The largest pandigital prime is", a)

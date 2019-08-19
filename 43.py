# This algorithm is written in Python 3.7
from time import time
start = time()


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


# Define the maximal pandigital
a = 9876543210
sum_nums = 0
primes = [2, 3, 5, 7, 11, 13, 17, 19]
# Run till the smallest 10-digit pandigital (including 0)
while a != 1023456789:
    # flag shows if the problem conditions are met
    flag = True
    s_a = str(a)
    for i in range(1, len(s_a)-2):
        # These are the problem conditions
        if int(s_a[i:i+3]) % primes[i-1] != 0:
            # if one of the conditions isn't met then exit from the loop
            flag = False
            break
    if flag:
        # addend the found number to sum
        sum_nums += a
        print(a)
    # Run the loop with the previous pandigital
    a = prev_pandigital(a)

print(sum_nums)
print("The answer took {:.2f} seconds".format(time() - start))

d_max = 1000  # The searching area, maximum for d
list_n = list()  # the list, where we will save all the values for n
# n is changing remainder, a found out that it repeats in cycles.
# If we stumble on it second time in the loop that means we found the cycle.
str_a = ''  # We will save here the sequence of all the digits
# The indexes of all the digits are corresponded to numbers in the list_n
length = -1  # We will write the maximal found length in this variable
found_d = -1  # And corresponding value for d will be here
for d in range(d_max, 1, -1):
    # Begin from the biggest numbers, because the chance to find maximal length here is bigger
    n = 1
    list_n.clear()
    str_a = ''
    while n > 0:  # We exit the loop if the number is not cycled
        n *= 10
        a = n // d
        if n in list_n:  # If the cycle is found
            if length < len(list_n) - list_n.index(n):
                # save the found length if it's less than others, which found before
                # calculate it using the index of previous n, which equals to last one
                length = len(list_n) - list_n.index(n)
                s = '0.' + str_a[:list_n.index(n)] + '(' + str_a[list_n.index(n):] + ')'
                found_d = d
            break
        else:
            str_a += str(a)  # save the last digit
            list_n.append(n)  # add the value for n
        n -= a * d
if found_d == -1:
    print("There's no cycles")
else:
    print("1 / {} = {}, \nwhere length of cycle is {}".format(found_d, s, length))

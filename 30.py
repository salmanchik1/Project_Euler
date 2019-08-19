# This program is written in Python 3.7
summ = 0
n = 5
powers_n = list(x**n for x in range(10))
print(powers_n)
num_set = set()


def check(depth, summ, number):
    if depth == 0:
        if summ == int(number) and int(number) > 9:
            num_set.add(int(number))
        return None
    for i in range(10):
        check(depth-1, summ + powers_n[i], str(i) + number)


check(n+1, 0, '')

print(num_set)
print(sum(num_set))

# This algorithm is written in Python 3.7
number = int(1e+6)
chain = dict()
max_steps = -1
long_chain_number = -1


def calc(n):
    global chain
    if str(n) in chain:
        return n, chain[str(n)]
    if n == 1:
        a, b = 1, 0
        chain['1'] = 0
        return a, b
    elif n % 2 == 0:
        a, b = calc(n//2)
        chain[str(n)] = b + 1
    else:
        a, b = calc(3*n+1)
        chain[str(n)] = b + 1
    # print(a, b)
    return n, b+1


for i in range(1, number):
    calc(i)
    if max_steps < chain[str(i)]:
        max_steps = chain[str(i)]
        long_chain_number = i
print("The longest chain number is {} \nIt consist {} steps".format(long_chain_number, max_steps))

# This algorithm is written in Python 3.7
def pandigital(num_str):
    if len(num_str) != len(num_str):
        return False
    my_set = set()
    for char in num_str:
        if char != '0' and int(char) <= len(num_str):
            my_set.add(char)
    return len(my_set) == len(num_str)


maximum = 0
for i in range(1, 10000):
    j = 1
    conc_str = ''
    while len(conc_str) < 9:
        conc_str += str(i * j)
        j += 1
    if pandigital(conc_str):
        if maximum < int(conc_str):
            maximum = int(conc_str)
        print(i, conc_str)

print("The max number made by concatenation is:", maximum)

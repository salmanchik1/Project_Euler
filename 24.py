# This solution is written in Python 3.7
n = 10
combinations = []
number = int(1e+6)
digits = {x for x in range(n)}


def run(my_list, string):
    global combinations
    if len(my_list) == 0:
        combinations.append(string)
    for c in my_list:
        run(my_list - {c}, string + str(c))
    return None


run(digits, '')
print(combinations[number-1])

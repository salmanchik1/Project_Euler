the_set = set(x for x in range(1, 10))
list_products = set()

def combination(myset, string):
    """gives all the permutations for set"""
    if len(myset) == 0:
        check(string)
        return None
    for i in myset:
        combination(myset - {i}, string + str(i))


def check(string):
    """checks the string permutation of digits"""
    product = int(string[5:])
    if int(string[0]) * int(string[1:5]) == product or int(string[0:2]) * int(string[2:5]) == product:
        list_products.add(product)
    pass


combination(the_set, '')
print(sum(list_products))

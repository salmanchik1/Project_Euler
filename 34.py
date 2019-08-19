#  This program is written in Python 3.7
dig_fact = list()
factorial = 1
summ = 0


def is_curious(value: str):
    """Checks if the number equals to the sum of the factorials of its digits"""
    return sum([dig_fact[int(digit)] for digit in value]) == int(value)


# calculate the list of factorials for all the digits instead 0
dig_fact.append(1)  # factorial of 0 is 0
for i in range(1, 10):
    factorial *= i
    dig_fact.append(factorial)
print(dig_fact)

# I used the upperbound 9! * 7 = 362880 * 7 = 2540160 because it's the maximal possible value
# it's less than 9999999
for i in range(10, dig_fact[9]*7 + 1):
    if is_curious(str(i)):
        print(i)
        summ += i
print("The sum of all curious numbers is:", summ)


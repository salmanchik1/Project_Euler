# This program is written in Python 3.7
import sympy
i = 11  # The first 2-digit prime to be larger that 7
summ = 0


def truncate(value):
    global summ
    for i in range(10):
        new_value = int(str(value) + str(i))
        if truncate_back(new_value) and new_value > 9:
            print(new_value)
            summ += new_value
        if sympy.isprime(new_value):
            truncate(new_value)


def truncate_back(value):
    if value > 0:
        if sympy.isprime(value):
            if value < 10:
                return True
            else:
                return truncate_back(int(str(value)[1:]))
        else:
            return False


truncate(0)
print("The sum is:", summ)

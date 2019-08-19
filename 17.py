# This program is written in Python 3.7
lengths = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4,
           10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,
           20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}
number = 1000
summ = 0
for i in range(1, number + 1):
    # a = number
    if i % 100 in range(10, 20):
        summ += lengths[i % 100]
    else:
        summ += lengths[i % 10]  # Add first order digits
        summ += lengths[i % 100 - i % 10]  # Second order digits in lieu of teens
    if i % 1000 >= 100:
        if i % 100 > 0:
            summ += 3  # "and"
        summ += lengths[(i % 1000) // 100]
        summ += 7  # "hundred"
        # if a % 1000 >= 200:
        #     sum_pence += 1  # hundred"s"
    if i >= 1000:
        summ += 11  # one thousand


print(summ)

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def convert(day, month, year):
    """Converts date to amount of days from Christmas"""
    value = 0
    month -= 1
    leap_year = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
    year -= 1
    value += year * 365
    value += year // 4
    value -= year // 100
    value += year // 400
    for i in range(month):
        value += months[i]
        if i == 1 and leap_year:
            value += 1
    value += day
    return value


counter = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if convert(1, m, y) % 7 == 0:
            counter += 1

print(counter)

# This program is written in Python 3.7
summ = 0
for i in range(int(1e+6)):
    dec_str = str(i)
    bin_str = str(bin(i))
    if bin_str[2:] == bin_str[:1:-1] and dec_str == dec_str[::-1]:
        summ += i
        print(dec_str, bin_str)
print(summ)

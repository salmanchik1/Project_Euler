# This algorithm is written in Python 3.7
length = 1000
fib_num_str = ['1', '1']
i = 2


def calc_sum(str1, str2):
    str3 = ''
    max_len = max(len(str1), len(str2))
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)
    flag = False
    for i in range(max_len-1, -1, -1):
        temp = int(str1[i]) + int(str2[i]) + int(flag)
        str3 = str(temp % 10) + str3
        if temp > 9:
            flag = True
        else:
            flag = False
    if flag:
        str3 = '1' + str3
    return str3


while len(fib_num_str[i-1]) < length:
    fib_num_str.append(calc_sum(fib_num_str[i-2], fib_num_str[i-1]))
    i += 1
print(i)

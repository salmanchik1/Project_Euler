res_num = 1
res_den = 1


def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a % b)


for s_num in range(1, 10):
    for s_den in range(s_num + 1, 10):
        for c_digit in range(1, 10):
            n1 = s_num * 10 + c_digit
            d1 = s_den * 10 + c_digit
            n2 = c_digit * 10 + s_num
            d2 = c_digit * 10 + s_den
            if s_num / s_den == n1 / d1:
                print("{} / {} = {} / {}".format(s_num, s_den, n1, d1))
            elif s_num / s_den == n1 / d2:
                print("{} / {} = {} / {}".format(s_num, s_den, n1, d2))
            elif s_num / s_den == n2 / d1:
                print("{} / {} = {} / {}".format(s_num, s_den, n2, d1))
            elif s_num / s_den == n2 / d2:
                print("{} / {} = {} / {}".format(s_num, s_den, n2, d2))
            else:
                continue
            res_den *= s_den
            res_num *= s_num

gcdivisor = gcd(res_num, res_den)
res_num = res_num // gcdivisor
res_den = res_den // gcdivisor
print("{} / {}".format(res_num, res_den))

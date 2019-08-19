sum = 1000
flag = False
A, B, C = 0, 0, 0
for a in range(1, sum - 1):
    for b in range(1, sum-a):
        c = sum - a - b
        if a**2 + b**2 == c**2:
            flag = True
            A = int(a)
            B = int(b)
            C = int(c)
            break
    if flag:
        break
print("The product of a Pythagorean triple {} + {} + {} = {} is {}".format(A, B, C, sum, A*B*C))

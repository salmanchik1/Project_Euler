def s_sum(value):
    value = int(value)
    if value > 0:
        return value + s_sum(value - 1)
    else:
        return 0


a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter max: "))
m -= 1
res = s_sum(m / a) * a + s_sum(m / b) * b - s_sum(m / (a * b)) * a * b
print("The sum equals: %i" % res)

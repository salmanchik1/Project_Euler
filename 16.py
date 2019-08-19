# This program is written in Python 3.7
n = 1000
num_list: list = [2]
temp: int = 0
for i in range(0, n-1):
    flag = False
    for j in range(len(num_list)-1, -1, -1):
        temp = num_list[j]
        temp *= 2
        if flag:
            temp += 1
            flag = False
        if temp > 9:
            flag = True
            num_list[j] = temp % 10
        else:
            num_list[j] = temp
    if flag:
        num_list.insert(0, 1)

print(sum(num_list))


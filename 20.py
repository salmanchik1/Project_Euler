# This program is written in Python 3.7
n = 100
s = [1]
for i in range(n):
    mem = 0
    for j in range(len(s)-1, -1, -1):
        val = s[j]
        val *= i + 1
        val += mem
        mem = val // 10
        s[j] = val % 10
    while mem > 0:
        s.insert(0, mem % 10)
        mem = mem // 10
print(sum(int(x) for x in s))

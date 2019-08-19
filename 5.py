# This algorithm written in Python 3.7
number = 1
maxim = 20
divs = list()
for i in range(2, maxim+1):
    temp = i
    for d in divs:
        if temp % d == 0:
            temp = int(temp / d)
    if temp > 1:
        divs.append(temp)

for i in divs:
    number *= i

print("The smallest number divisible by all the numbers "
      "from 1 to {} is {}".format(maxim, number))
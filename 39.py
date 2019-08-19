# This program is written in Python 3.7
num = 1000
# The maximal sum
squares = [i**2 for i in range(1, num // 2)]
# The length of the hypotenuse can't be larger than a half of a sum
sums = [0 for i in range(num)]
# Create the list filled by the zeros for each of the numbers
for i in range(3, num // 2 + 1):
    for c1 in range(1, i):
        # The length of a catheter couldn't be larger than the length of a hypotenuse
        for c2 in range(1, c1):
            # cut out all the duplications of the catheters with the rule that the c1 > c2
            if i + c1 + c2 > num:
                # also cut out all exceeding cases
                break
            if (squares[c1 - 1] + squares[c2 - 1]) == squares[i - 1]:
                # write down the case into the list of sums
                sums[i + c1 + c2 - 1] += 1
maximum = max(sums)  # find the maximum in the list of sums
print("The number", sums.index(maximum) + 1, "has the maximal amount of solutions - ", maximum)

# This program is written in Python 3.7
n = 20
grid = list()
for i in range(0, n+1):
    grid.append(list())
    for j in range(0, n+1):
        if i == 0 or j == 0:
            grid[i].append(1)
        else:
            grid[i].append(grid[i][j-1]+grid[i-1][j])
print("There are {} routes for n = {}".format(grid[n][n], n))

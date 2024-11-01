#3:14 - 4:15
grid = open('AoC_22/D8/input.txt').read().splitlines()
ROW = len(grid)
COL = len(grid[0])

res = 2 * (ROW + COL - 2)
for r in range(1, ROW-1):
    for c in range(1, COL-1):
        if all([grid[r][c] > grid[k][c] for k in range(r-1, -1, -1)]):
            res += 1
        elif all([grid[r][c] > grid[k][c] for k in range(r+1, ROW)]):
            res += 1
        elif all([grid[r][c] > grid[r][k] for k in range(c-1, -1, -1)]):
            res += 1
        elif all([grid[r][c] > grid[r][k] for k in range(c+1, COL)]):
            res += 1   
 
print(res)
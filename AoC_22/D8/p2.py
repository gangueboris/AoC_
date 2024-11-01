#3:40 - 4:12
grid = open('AoC_22/D8/input.txt').read().splitlines()
ROW = len(grid)
COL = len(grid[0])
def solve(grid, r, c, dr, dc):
    count = 0
    nr, nc = r + dr, c + dc
    while 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        if grid[nr][nc] >= grid[r][c]:
            count += 1
            break
        count += 1
        nr += dr
        nc += dc
    return count
    
res = 0
for r in range(1, ROW-1):
    for c in range(1, COL-1):
        mult = solve(grid, r, c, -1, 0) * solve(grid, r, c, 1, 0) * solve(grid, r, c, 0, -1) * solve(grid, r, c, 0, 1) 
        res = max(res, mult)      
       
print(res)
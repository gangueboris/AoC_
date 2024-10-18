# This problem is a mahattan distance computation problem.

grid = open("in.txt").read().splitlines()

ROW = len(grid)
COL = len(grid[0])
coords = [(r, c) for r in range(ROW) for c in range(COL) if grid[r][c] == '#']
empty_rows = [r for r in range(ROW) if all(grid[r][c] == '.' for c in range(COL))]
empty_cols = [c for c in range(COL) if all(grid[r][c] == '.' for r in range(ROW))]

ans = 0
scale = 1000000
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        r1, c1 = coords[i]
        r2, c2 = coords[j]

        for r in range(min(r1, r2), max(r1, r2)):
            ans += scale if r in empty_rows else 1
        
        for c in range(min(c1, c2), max(c1, c2)):
            ans += scale if c in empty_cols else 1
      
print(ans)
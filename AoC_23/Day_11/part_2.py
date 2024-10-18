# This problem is a mahattan distance computation problem.

grid = open('Day_11/input.txt', 'r').read().splitlines()

coords = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '#']

empty_rows = [r for r in range(len(grid)) if all([grid[r][c] == '.' for c in range(len(grid[0]))])]
empty_cols = [c for c in range(len(grid[0])) if all([grid[r][c] == '.' for r in range(len(grid))])]

ans = 0
scale = 1000000

for i in range(len(coords)):
    for j in range(i + 1, len(coords)): # To avoid duplicate
        x1, y1 = coords[i]
        x2, y2 = coords[j]

        for r in range(min(x1, x2), max(x1, x2)): # move trough row
            ans += scale if r in empty_rows else 1

        for c in range(min(y1, y2), max(y1, y2)): # move trough column
            ans += scale if c in empty_cols else 1

print(ans) # 692506533832
        
        

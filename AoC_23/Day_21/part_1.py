# Today problem is about counting steps in a 2D grid
from collections import deque

grid = open("Day_21/in.txt", 'r').read().splitlines()
start = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            start = (r, c)
            break

visited = set()
steps = 6
q = deque([(start[0], start[1], steps)])
ans = set()
while q:
    r, c, steps = q.popleft()
    if steps % 6 == 0:
        ans.add((r, c))
    if steps == 0:
        break
    if (r, c) in visited:
        continue
    visited.add((r, c))

    for rn, cn in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if rn < 0 or rn > len(grid) or cn < 0 or cn > len(grid[0]) or grid[rn][cn] == '#' or (rn, cn) in visited:
            continue
        q.append((rn, cn, steps - 1))


            


          
          

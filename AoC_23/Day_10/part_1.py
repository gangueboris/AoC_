from collections import deque
grid = open('in.txt').read().splitlines()
ROW = len(grid)
COL = len(grid[0])

start = [(r, c) for r in range(ROW) for c in range(COL) if grid[r][c] == 'S']

visited = {start[0]}
q = deque(start)

while q:
    r, c = q.popleft()
    ch = grid[r][c]
    
    if r - 1 >= 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in visited:  # TOP
        visited.add((r - 1, c))
        q.append([r - 1, c])
    
    if r + 1 < ROW and ch in "S|7F" and grid[r +1][c] in "|JL" and (r + 1, c) not in visited:  # BOTTOM
        visited.add((r + 1, c))
        q.append([r + 1, c])
    
    if c + 1 < COL and ch in "S-LF" and grid[r][c + 1] in "-7J" and (r, c + 1) not in visited: # RIGHT
        visited.add((r, c + 1))
        q.append([r, c + 1])
    
    if c - 1 >= 0 and ch in "S-7J" and grid[r][c - 1] in "-LF" and (r, c -1) not in visited:   # LEFT
        visited.add((r, c - 1))
        q.append([r, c - 1])

print(len(visited) // 2)
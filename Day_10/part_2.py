"""
NOTE: I suppose to return the total and pipe, tile which are in the loop.
QUESTIONS: How to know if a position is inside or outside the loop ?
Intuition: remarking that the loop forms a geometric figure (polygon), we can apply 'ray casting alogorithm'.
Approch: (ray algorithm)
For any point in the grid, if line drawing for that point to left or right direction, if that line cross odd time the 
polygon, it means that the point is inside the polygon otherwise it is outside.
NB: Here 0 is consider like even number.
"""
from collections import deque

grid = open('Day_10/test.txt', 'r').read().splitlines()

def findStart(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                return (r, c)

def moves(grid, r, c, rn, cn):
    pos = [rn - r, cn - c]
    ch = grid[r][c]

    if ch in "S|7F" and pos == [1, 0] and grid[rn][cn] in "|JL":                        
        return True
    elif ch in "S|JL" and  pos == [-1, 0] and grid[rn][cn] in "|7F":                        
        return True
    elif ch in "S-J7" and pos == [0, -1] and grid[rn][cn] in "-FL":                         
        return True
    elif ch in "S-FL" and pos == [0, 1] and grid[rn][cn] in "-J7":                       
        return True
    return False


def isValid(grid, r, c, rn, cn):
    return 0 <= rn < len(grid) and 0 <= cn < len(grid[0]) and moves(grid, r, c, rn, cn)

    
def bfs(grid):
    visited = set()
    q = deque([findStart(grid)])

    while q:
        r, c = q.popleft()
    
        if (r, c) not in visited:
            visited.add((r, c))
        
        for rn, cn in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
            if (rn, cn) not in visited and isValid(grid,r, c, rn, cn):
                q.append((rn, cn))
    return visited

def inside(grid, poly_limit):
    count = 0
    for r in range(len(grid)):
        crossing = 0
        for c in range(len(grid[0])):
            if (r, c) in poly_limit:
                if grid[r][c] in "|LJ":
                   crossing += 1
            else:
                if crossing % 2 == 1:
                    count += 1
    return count

print(inside(grid, bfs(grid))) # 

from collections import deque
## This is a <labyrinth>, finding shortest path problem ##

grid = open('Day_10/input.txt', 'r').read().splitlines()

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

    
def solve (grid):
    visited = set()
    q = deque([findStart(grid)])
    distances = [[0] * len(grid[0]) for _ in grid]
    ans = 0

    while q:
        r, c = q.popleft()
        curr_dist = distances[r][c]

        if (r, c) not in visited:
            visited.add((r, c))
        
        for rn, cn in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
            if (rn, cn) not in visited and isValid(grid,r, c, rn, cn):
                q.append((rn, cn))
                distances[rn][cn] = curr_dist + 1
                ans = max(ans, distances[rn][cn])

    return ans

print(solve(grid)) # 6682



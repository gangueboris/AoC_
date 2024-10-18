ans = 0
def isSym(grid, i): # This  function is like palindrom but on a grid:Two pointer approch
    lower = i
    upper = i + 1
    while lower >= 0 and upper < len(grid):
        if grid[lower] != grid[upper]:
            return False
        lower -= 1
        upper += 1
    return True

def findSym(grid):
    for i in range(len(grid) - 1):
        if isSym(grid, i):
            return i + 1
    return 0

def transpose(grid): # Transpose vertical to horizontal
    return [list(line) for line in zip(*grid)]

for grid in open('in.txt').read().split('\n\n'):
    grid = grid.split('\n')
    ans += 100 * findSym(grid)
    ans += findSym(transpose(grid))

print(ans)
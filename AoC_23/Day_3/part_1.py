"""
NOTE: 
- when I have  grid to process, initialize the len(row) and len(col) to the optimization
- This problem is about finding a number in a grid and look around if that number is valid.

"""
def isdigit(c):
    return True if ord(c) >= 48 and ord(c) <= 57 else False

grid = open('Day_3/input.txt').read().splitlines()
ans = 0
row = len(grid)
col = len(grid[0])
for r, line in enumerate(grid):
    i = 0
    while i < col:
        num = ""
        while i < col and isdigit(line[i]):
            num += line[i]
            i += 1

        start = i - len(num)
        end = i - 1
        i += 1
        if start - 1 >= 0 and not isdigit(grid[r][start - 1]) and grid[r][start - 1] != '.': # LEFT
            ans += int(num) if num else 0
            continue

        if end + 1 < col and not isdigit(grid[r][end + 1]) and grid[r][end + 1] != '.':  # RIGHT
            ans += int(num) if num else 0
            continue

        if r - 1 >= 0: # TOP
            for c in range(start - 1, end + 2):
                if c >= 0 and c < col and not isdigit(grid[r - 1][c]) and grid[r - 1][c] != '.':
                    ans += int(num) if num else 0
                    continue
        
        if r + 1 < row: # BOTTOM
            for c in range(start - 1, end + 2):
                if c >= 0 and c < col and not isdigit(grid[r + 1][c]) and grid[r + 1][c] != '.':
                    ans += int(num) if num else 0
                    continue
print(ans)
            

                

        


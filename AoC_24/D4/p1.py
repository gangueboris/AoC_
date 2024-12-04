grid = open('AoC_24\D4\input.txt').read().splitlines()

word = "XMAS"

def getDiagonals(grid):
    rows = len(grid)
    cols = len(grid[0])
    diagonals = []

    # Top-left to bottom-right diagonals
    for d in range(-(rows - 1), cols): 
        diag = ""
        for i in range(rows):
            j = d + i  
            if 0 <= j < cols:  
                diag += grid[i][j]
        if diag:
            diagonals.append(diag)

    # Top-right to bottom-left diagonals
    for d in range(cols + rows - 1): 
        diag = ""
        for i in range(rows):
            j = d - i  
            if 0 <= j < cols:  
                diag += grid[i][j]
        if diag:
            diagonals.append(diag)

    return diagonals


def HoriVert(line, word):
    l = 0
    count = 0
    reWord = word[::-1]

    for r in range(1, len(line)):
        if line[r] == 'X':
            l = r
        if word in line[l: r+1]:
            l = r
            count += 1
    l = 0
    for r in range(1, len(line)):
        if line[r] == 'S':
            l = r
        if reWord in line[l: r+1]:
            l = r
            count += 1

    return count

ans = 0
# Hirizontal
for r in range(len(grid)):
    ans += HoriVert(grid[r], word)

temp = ""
# Vertical
for c in range(len(grid[0])):
    for r in range(len(grid)):
       temp += grid[r][c]
    ans += HoriVert(temp, word)
    temp = ""

for diag in getDiagonals(grid):
    ans += HoriVert(diag, word)



print(ans)


grid = open('AoC_24\D4\input.txt').read().splitlines()

word = "MAS"
reWord = word[::-1]
ans = 0


for r in range(1, len(grid)-1):
    for c in range(1, len(grid[0])-1):
        if grid[r][c] == 'A':
            temp1 = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
            temp2 = grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1]
            if temp1 == word and temp2 == word:
                ans += 1
            elif temp1 == reWord and temp2 == reWord:
                ans += 1
            elif temp1 == word and temp2 == reWord:
                ans += 1
            elif temp1 == reWord and temp2 == word:
                ans += 1

print(ans)


from collections import defaultdict
def isdigit(c):
    return True if ord(c) >= 48 and ord(c) <= 57 else False

grid = open('in.txt').read().splitlines()
ans = 0
row = len(grid)
col = len(grid[0])

storage = defaultdict(list)

for r, line in enumerate(grid):
    i = 0
    while i < col:
        num = ""
        while i < col and ord(line[i]) >= 48 and ord(line[i]) <= 57:
            num += line[i]
            i += 1

        start = i - len(num)
        end = i - 1
        i += 1
        if start - 1 >= 0 and grid[r][start - 1] == '*': # LEFT
            if num:
               storage[(r, start - 1)].append(int(num))
            continue

        if end + 1 < col and grid[r][end + 1] == '*':  # RIGHT
            if num:
               storage[(r, end + 1)].append(int(num))
            continue

        if r - 1 >= 0: # TOP
            for c in range(start - 1, end + 2):
                if c >= 0 and c < col and grid[r - 1][c] == '*':
                    if num:
                        storage[(r - 1, c)].append(int(num))
                    continue
        
        if r + 1 < row: # BOTTOM
            for c in range(start - 1, end + 2):
                if c >= 0 and c < col and grid[r + 1][c] == '*':
                    if num:
                       storage[(r + 1, c)].append(int(num))
                continue

for liste in storage.values():
    if len(liste) == 2:
        ans += int(liste[0]) * int(liste[1])

print(ans)
            
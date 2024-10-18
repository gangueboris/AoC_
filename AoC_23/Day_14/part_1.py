"""
1. Tilt the platform by moving
- find the new position of O
2. find the position and add up 
- positon = len(platerform) - i    i in (0 - len(platerform) - 1)

NOTICE: This problem is talking about moving and element for buttom to top in their column by paying attention to obstacles
"""
plt = open('Day_14/input.txt','r').read().splitlines()

def tilted(plt):
    new_plt = [[c if line[i] == '#' else '.' for i, c in enumerate(line)] for line in plt]
    for r in range(len(plt)):
        for c in range(len(plt[0])):
            if plt[r][c] == 'O':
                row_up = r - 1
                while row_up >= 0 and new_plt[row_up][c] == '.': # Trying to find the correct position to insert the 'O'
                    row_up -= 1  
                new_plt[row_up + 1][c] = 'O'
    return new_plt

plt = tilted(plt)

ans = 0
plt_len = len(plt)
for i, line in enumerate(plt):
    ans += (plt_len - i) * line.count('O')

print(ans) # 113456

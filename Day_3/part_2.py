content = open("Day_3/input.txt", 'r').read().splitlines()

"""
Gear ratio: product exactly two part numbers adjacents to any '*'
Goal : find a gear ratio: add them uyp end return the result.

Approch:
temp = {}
- find a part number associate to '*',
I will first check if the coordonate of that '*' is temp:
 if not: temp[(coordonate)] = []
 else: temp[(coordonate)].append(partNumber)

- At the end of the exploration, I will iterate through temp by checking which value has length of 2; make the product between them and
add up to my result.

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def isstarsymbol(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '*'

def findGear(grid):
    temp = {}
    for r in range(len(grid)):
        c = 0
        while c < len(grid[0]):
            digit = ''
            while c < len(grid[0]) and grid[r][c].isdigit():
                digit += grid[r][c]
                c += 1
            if digit == '':
                c += 1
                continue
            number = int(digit)
            start, end = c - len(digit), c - 1

            if isstarsymbol(grid, r, start - 1):
                if (r, start - 1) not in temp:
                    temp[(r, start - 1)] = []
                    temp[(r, start - 1)].append(number)
                else:
                    temp[(r, start - 1)].append(number)
                continue
            elif isstarsymbol(grid, r, end + 1):
                if (r, end + 1) not in temp:
                    temp[(r, end + 1)] = []
                    temp[(r, end + 1)].append(number)
                else:
                    temp[(r, end + 1)].append(number)
                continue

            for k in range(start - 1, end + 2):
                if isstarsymbol(grid, r + 1, k):
                    if (r + 1, k) not in temp:
                        temp[(r + 1, k)] = []
                        temp[(r + 1, k)].append(number)
                    else:
                        temp[(r + 1, k)].append(number)
                    break
                elif isstarsymbol(grid, r - 1, k):
                    if (r - 1, k) not in temp:
                        temp[(r - 1, k)] = []
                        temp[(r - 1, k)].append(number)
                    else:
                        temp[(r - 1, k)].append(number)
                    break
    res = 0

    for val in temp.values():
        if len(val) == 2:
            res += val[0] * val[1]
    return res


print(findGear(content))  # 80253814
                

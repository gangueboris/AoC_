content = open('Day_3/test.txt', 'r').read().splitlines()
"""
Goal: add up all part numbers

A part number is a number which is adjacent even in diagonal to a symbol.
NB: '.' is not considered like a symbol.

Approch:
- Browse the input in goal to find a number
- if number find, generate neighbbour table and explore around
- if we meet in the exploration something different than '.' && !isdigit(grid[r][c]) and up the number to res
 

input:
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

1. use the algorithm of flood filling

"""
"""
def findPartNumber(grid):
    res = 0
    for r in range(len(grid)):
        digit = ''
        for c in range(len(grid[0])):
            if grid[r][c].isdigit():
                digit += grid[r][c]
            else:
                if digit != '':
                    #print(digit)
                    for rn, cn in  findNeighbours(digit): # generate (rn, cn) of (digit)
                        rowBounds = 0 <= rn < len(grid)
                        colsBounds = 0 <= cn < len(grid[0])
                        if rowBounds and colsBounds and grid[rn][cn] != '.' and not grid[rn][cn].isdigit():
                            res += int(digit)

                    digit = ''
    return res

    

findPartNumber(content)
"""

with open('Day_3/test.txt', 'r') as fin:
    data = fin.read()
    lines = data.strip().split("\n")

n = len(lines)
m = len(lines[0])


def is_symbol(i, j):
    return 0 <= i < n and 0 <= j < m and lines[i][j] != "." and not lines[i][j].isdigit()
       
ans = 0

for i, line in enumerate(lines): # each row and line
    start = 0
                        # start & j € [colomn]
    j = 0

    while j < m: # iterate over the column, takes each character one by one
        start = j # why putting there and note in the coming loop ?
        num = ""
        while j < m and line[j].isdigit(): # when I find a starting number of a digit, looping to form the entire number
            num += line[j] # add up to constitute the number
            j += 1

        if num == "": # when a character is not a starting digit of a number, ignore the rest of the code and move to the next iteration
            j += 1
            continue

        num = int(num) # convert the founded number to an integer

        # Number ended, look around
        if is_symbol(i, start-1) or is_symbol(i, j): # first look at left and right, if there is a symbol, add up the number to ans and move on
            ans += num
            continue

        for k in range(start-1, j+1): # j+1 to take in account the j
            if is_symbol(i-1, k) or is_symbol(i+1, k): # tcheck at the time down and top of each digit of the number including top and down of the left and right
                ans += num
                break

print("result: ", ans)

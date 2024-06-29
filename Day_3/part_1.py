content = open('Day_3/input.txt', 'r').read().splitlines()
"""
Goal: add up all part numbers

A part number is a number which is adjacent even in diagonal to a symbol.
NB: 
- '.' is not considered like a symbol.
- Does forget to take in account the last number on a row
Approch:
- Browse the input in goal to find a number
- if number find explore around 
- if we meet in the exploration something different than '.' && !isdigit(grid[r][c]) and up the number to res and directly move to the next iteration

Time complexity: O(n * m)
Space complexity O(1)
 

input:
467..114..
...*......
..35..6330  <-- Here
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

1. use the algorithm of flood filling
"""
def isSymbol(grid, r, c):
    rowBounds = 0 <= r < len(grid)
    colsBounds = 0 <= c < len(grid[0])
    return rowBounds and colsBounds and grid[r][c] != '.' and not grid[r][c].isdigit()

def findPartNumber(grid):
    res = 0
    for r in range(len(grid)):
        digit = ''
        c = 0
        while c < len(grid[0]):
            digit = ''
            while c < len(grid[0]) and grid[r][c].isdigit(): # Ierate to find a number and ensuring that even a number at the end of row is taken in account
                digit += grid[r][c]
                c += 1
           
            if digit == '':  # if this character in the row doesn't start witha a digit, move to the next character
                c += 1
                continue

            # looks left and right of the number
            start, end = c - len(digit), c -1    # ... are position in column
            #print([digit, start, end])
            if isSymbol(grid, r, start - 1) or isSymbol(grid, r, end + 1): # looks left and right the number
                res += int(digit) 
                continue # find now move to the next iteration

            for k in range(start - 1, end + 2): 
                if isSymbol(grid, r - 1, k) or isSymbol(grid, r + 1, k): # tcheck at the time down and top of each digit of the number including top and down of the left and right
                    res += int(digit)
                    break # to note count multiple time when we have several symbol around the number
                    
    return res

    
print(findPartNumber(content))

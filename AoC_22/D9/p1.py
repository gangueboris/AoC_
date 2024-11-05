#7:04, 5:14
#create grid
#read the data on move in the grid
input = open('AoC_22/D9/input.txt').read().splitlines()
input = [(elem.split()[0], int(elem.split()[1])) for elem in input]

def findHW(input):
    w, h = 0, 0
    for v, n in input:
        if v == 'R' or v == 'L':
            w = max(w, n)
        else:
            h = max(h, n)
    return (h, w)

h, w = findHW(input)
grid = [[0 for _ in range(2*w)] for _ in range(2*h)]
hx, hy = w, h # I will create a 2* W x 2 * H grid
tx, ty = w, h
"""
- If the head is ever two steps directly up, down, left,
 or right from the tail, the tail must also move one step in 
 that direction 
 - if the head and tail aren't touching and aren't in the
   same row or column, the tail always moves one step
   diagonally to keep up

   func: checked if touching(grid, hx, hy, tx, ty)
   func: move_tail(grid, hx, hy, tx, ty)
"""
def isTouching(hx, hy, tx, ty):
    varx = abs(hx - tx) 
    vary = abs(hy - ty) 
    if (varx == 1 and vary == 0) or (varx == 0 and vary == 1) or (varx == 1 and vary == 1) or (varx == 0 and vary == 0):
        return True
    return False

def whereToMove(hx, hy, tx, ty):
    varx = hx - tx 
    vary = hy - ty 
    if varx == 0:             #top-down
        if vary > 0:
            return 'D'
        elif vary < 0:
            return 'U'
    elif vary == 0:         # left-right
        if varx > 0:
            return 'R'
        elif varx < 0:
            return 'L'
    else:                    # diag
        if ty > hy: # top-left or top-right
            if tx < hx:
                return 'UR'
            elif tx > hx:
                return 'UL'
        elif ty < hy:
            if tx > hx:
                return 'DL'
            elif tx < hx:
                return 'DR'

def moveTail(newPos, tx, ty):
    mapping = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0),'UL': (-1, 1), 'UR': (1, 1), 'DL': (-1, -1), 'DR': (1, -1)}
    tx += mapping[newPos][0]
    ty += mapping[newPos][1]
    return (tx, ty)

for dir, pos in input:
    if dir == 'R':
        hx += pos
    elif dir == 'L':
        hx -= pos
    elif dir == 'U':
        hy += pos
    else:
        hy -= pos

    if not isTouching(hx, hy, tx, ty):
       print(tx, ty)
       tx, ty = moveTail(whereToMove(hx, hy, tx, ty), tx, ty)
       print(tx, ty)
    
        
#7:04, 5:14, 5:11 
#create grid
#read the data on move in the grid
"""
============== ADVICE ===================
When you are delling with a problem which talk about moving in different direction:
Walk through this steps:
1. At which condition can I move ?
2. In which directions I allow to move ? (Vertical, Horizontal and Diagonal)
3. From a direction, in which sens I can move ? (left and right)
"""
visited = set([0, 0])
H = [0, 0]
T = [0, 0]
for line in open('AoC_22/D9/input.txt').read().splitlines():
    d, v = line.split()
    v = int(v)
    for _ in range(v):
        H[0] += 1 if d == 'R' else -1 if d == 'L' else 0
        H[1] += 1 if d == 'U' else -1 if d == 'D' else 0

        dx = H[0] - T[0]
        dy = H[1] - T[1]
        
        if abs(dx) > 1 or abs(dy) > 1:
            if dx == 0:
                T[1] += 1 if dy > 0 else -1
            elif dy == 0:
                T[0] += 1 if dx > 0 else -1
            else:
                T[0] += 1 if dx > 0 else -1
                T[1] += 1 if dy > 0 else -1

        visited.add(tuple(T))

print(len(visited) - 1)






















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
hx, hy = 0, 4 # I will create a 2* W x 2 * H grid
tx, ty = 0, 4

for dir, pos in input:
    for p in range(1, pos + 1):
        if dir == 'R':
            hx += p
        elif dir == 'L':
            hx -= p
        elif dir == 'U':
            hy += p
        else:
            hy -= p

        if not isTouching(hx, hy, tx, ty):
            print( tx, ty)
            tx, ty = moveTail(whereToMove(hx, hy, tx, ty), tx, ty)
    
"""    
        
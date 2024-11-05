#4:54 - (Understand the problem: 5:26)
from collections import defaultdict
#6:08
cwd = defaultdict(defaultdict)
root = defaultdict(defaultdict)
for line in open('AoC_22/D7/input.txt').read().splitlines():
    line = line.strip()
    if line[:4] == '$ cd':
        dir = line[5:]
        if dir == '/':
            cwd = root
            stack = []
        elif dir == '..':
            cwd = stack.pop()
        else:
            if dir not in cwd:
               cwd[dir] = defaultdict(defaultdict)
            stack.append(cwd)
            cwd = cwd[dir]

    elif line[0] != '$':
        size, file = line.split()
        if size == 'dir':
            cwd[file] = defaultdict(defaultdict)
        else:
            cwd[file] = int(size)

def findRootSize(dir = root):
    if type(dir) == int:
        return (dir)
    total = 0
    for child in dir.values():
        total += findRootSize(child)
    return (total)
            
def findDirSize(dir, dirSizes):
    if type(dir) == int:
        return (dir)
    total = 0
    for child in dir.values():
        total += findDirSize(child, dirSizes)
    dirSizes.append(total)
    return (total)


required = 30000000
unused = 70000000 - findRootSize()
dirSizes = []
findDirSize(root, dirSizes)
dirSizes.sort()
for val in dirSizes:
    if val + unused >= required:
       print(val)
       break


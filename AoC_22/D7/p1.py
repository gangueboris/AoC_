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

def solve(dir = root):
    if type(dir) == int:
        return (dir, 0)
    size = 0
    ans = 0
    for child in dir.values():
        s, a = solve(child)
        size += s
        ans += a

    if size <= 100000:
        ans += size
    return (size, ans)


print(solve()[1])

 
from collections import defaultdict
import math
LR, *nodes = open('Day_8/input.txt', 'r').read().splitlines()
graph = defaultdict(chr)

starts = []
for line in nodes[1:]:
    node, neighours = line.split(' = ')
    a, b = neighours.split(', ')
    a = a[1:]
    b = b[0:3]
    graph[node] = (a, b)
    if node[2] == 'A':
        starts.append(node)

lens = []
for s in starts:
    i = 0
    current = s
    while current[2] != 'Z':

        if LR[i % len(LR)] == 'L':
            current = graph[current][0]
        else:
            current = graph[current][1]
            
        i += 1
    lens.append(i)
ans = math.lcm(*lens)

print(ans)  # 17099847107071   

        

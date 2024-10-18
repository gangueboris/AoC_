from collections import defaultdict
from math import lcm
directions, connections = open('in.txt').read().split('\n\n')
graph = defaultdict(list)
starts = []
for line in connections.split('\n'):
    node, rest = line.split(' = ')
    rest = rest[1:-1].split(', ')
    graph[node] = rest
    if node[2] == 'A':
        starts.append(node)


length = len(directions)
stepsList = []
for current in starts:
    steps = 0
    while current[2] != 'Z':
        pos = directions[steps % length]
        if pos == 'L':
            current = graph[current][0]
        else:
            current = graph[current][1]
        steps += 1
    stepsList.append(steps)
print(stepsList)

print(lcm(*stepsList))

from collections import defaultdict
directions, connections = open('in.txt').read().split('\n\n')
graph = defaultdict(list)
for line in connections.split('\n'):
    node, rest = line.split(' = ')
    rest = rest[1:-1].split(', ')
    graph[node] = rest

steps = 0
current = 'AAA'
length = len(directions)
while current != 'ZZZ':
    pos = directions[steps % length]
    if pos == 'L':
        current = graph[current][0]
    else:
        current = graph[current][1]
    steps += 1
print(steps)



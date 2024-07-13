from collections import defaultdict

LR, *nodes = open('Day_8/input.txt', 'r').read().splitlines()
graph = defaultdict(chr)

for line in nodes[1:]:
    node, neighours = line.split(' = ')
    a, b = neighours.split(', ')
    graph[node] = (a[1:], b[0:3])


i = 0
current = 'AAA'
while current != 'ZZZ':
    if LR[i % len(LR)] == 'L':
        current = graph[current][0]
    else:
        current = graph[current][1]
    i += 1

print(i) # 19099

        

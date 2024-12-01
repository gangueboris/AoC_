visited = set([0, 0])
H = [0, 0]

nodes = [[0, 0] for _ in range(9)]

for line in open('AoC_22/D9/input.txt').read().splitlines():
    d, v = line.split()
    v = int(v)
    for _ in range(v):
        H[0] += 1 if d == 'R' else -1 if d == 'L' else 0
        H[1] += 1 if d == 'U' else -1 if d == 'D' else 0
         
        curr = H
        for i in range(len(nodes)):
            T = nodes[i]
            dx = curr[0] - T[0]
            dy = curr[1] - T[1]
            
            if abs(dx) > 1 or abs(dy) > 1:
                if dx == 0:
                    T[1] += 1 if dy > 0 else -1
                elif dy == 0:
                    T[0] += 1 if dx > 0 else -1
                else:
                    T[0] += 1 if dx > 0 else -1
                    T[1] += 1 if dy > 0 else -1
            curr = T

        visited.add(tuple(nodes[8]))

print(len(visited) - 1)


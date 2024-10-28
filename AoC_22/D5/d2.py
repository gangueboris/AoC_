# 8: 25 PM 9:35
from collections import defaultdict
mapping = defaultdict(list)

stacks, moves = open('AoC_22/D5/input.txt').read().split("\n\n")
stacks = stacks.split('\n')
nbres = [int(n) for n in stacks[-1].split()]

movs = []
for m in moves.split('\n'):
    _, a, _, b , _, c = m.split()
    movs.append((int(a), int(b), int(c)))

for line in stacks[:-1]:
    k = 0
    i = 0
    temp = line.split(' ')
    while k < len(temp):
        if temp[k] == '':
            k += 3
            i += 1
        else:
            mapping[nbres[i]].append(temp[k])
            i += 1
        k += 1

for n, src, dest in movs:
    for i in range(n):
        mapping[dest].insert(i, mapping[src][0])
        mapping[src].remove(mapping[src][0])

mapping = dict(sorted(mapping.items()))
res = ''
for v in mapping.values():
    res += v[0][1]

print(res)
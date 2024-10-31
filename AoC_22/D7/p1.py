#4:54 - (Understand the problem: 5:26)
from collections import defaultdict
input = open('AoC_22/D7/input.txt').read().splitlines()
mapping = defaultdict(list)
mappingChar = defaultdict(list)
repo = ''
prev = ''
mapInt = defaultdict(int)
for i, line in enumerate(input):
    if line[2:4] == 'cd':
        repo = line[5:]
        prev = input[i+1]
        continue
    if prev == "$ ls" and line != "$ ls":
        n, r = line.split()
        if n != 'dir':
           mapping[repo].append(int(n))
        else:
            mappingChar[repo].append(r)

for k, v in mapping.items():
    mapInt[k] = sum(v)
for k, v in mappingChar.items():
    for elem in v:
      mapInt[k] += mapInt[elem]

res = 0
for elem in mapInt.values():
    if elem <= 100000:
        res += elem
print(res)
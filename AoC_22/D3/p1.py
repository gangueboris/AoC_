#7:30 : 8:03
res = 0
for line in open('AoC_22/D3/input.txt').read().splitlines():
    checked = set()
    n = len(line) // 2
    first = line[:n]
    second = line[n:]
    for c in first:
        if c in second and c not in checked:
            if c.islower():
                res += ord(c) - 96
            else:
                res += ord(c) - 38
            checked.add(c)
print(res)
 
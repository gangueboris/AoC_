input = open('AoC_24/D1/input.txt').read().splitlines()
Lrecord = sorted([int(line.split()[0]) for line in input])
Rrecord = sorted([int(line.split()[1]) for line in input])

total = 0
for l, r in zip(Lrecord, Rrecord):
    total += abs(l - r)
print(total)


       



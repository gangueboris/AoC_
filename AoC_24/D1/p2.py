input = open('AoC_24/D1/input.txt').read().splitlines()
Lrecord = sorted([int(line.split()[0]) for line in input])
Rrecord = sorted([int(line.split()[1]) for line in input])

total = 0
for l in Lrecord:
    count = 0
    for r in Rrecord:
        if l == r:
            count += 1
    total += (l * count)



print(total)


       



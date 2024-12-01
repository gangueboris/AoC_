X = 1
cycle = 0
ans = 0
n = 2
for line in open("AoC_22/D10/input.txt").read().splitlines():
    line = line.strip()
    if line[0] == 'n':
        cycle += 1
        if cycle == 20 or not (cycle + 20) % 40:
            ans += cycle * X
    else:
        cmd, v = line.split()
        for _ in range(n):
            cycle += 1
            if cycle == 20 or not (cycle + 20) % 40:
                ans += cycle * X
        X += int(v)

print(ans)


 


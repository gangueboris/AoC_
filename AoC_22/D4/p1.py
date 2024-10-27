#11: 10 11: 24
res = 0
def contains(a, b, d, e):
    if a <= d <= b and a <= e <= b:
        return True
    return False

for line in open('AoC_22/D4/input.txt').read().splitlines():
    one, sec = line.split(',')
    a, b = [int(c) for c in one.split('-')]
    d, e = [int(c) for c in sec.split('-')]
    if contains(a, b, d, e) or contains(d, e, a, b):
        res += 1

print(res)

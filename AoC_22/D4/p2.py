#11: 10 11: 24 p2: 11:49
res = 0
def overlap(a, b, d, e):
    if (d < a  and a <= e < b) or (a < d <= b and e > b) or (a <= d <= b and a <= e <= b):
        return True
    return False

for line in open('AoC_22/D4/input.txt').read().splitlines():
    one, sec = line.split(',')
    a, b = [int(c) for c in one.split('-')]
    d, e = [int(c) for c in sec.split('-')]
    if overlap(a, b, d, e) or overlap(d, e, a, b):
        res += 1

print(res)

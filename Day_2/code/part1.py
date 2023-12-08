from collections import defaultdict
with open("Day_2\Docs&Images\input_Day2_part1.txt","r") as file:
    content = file.read()
"""
p1 = 0
p2 = 0
for line in content.split('\n'):
    ok = True
    id_, line = line.split(':')
    V = defaultdict(int)
    for event in line.split(';'):
        for balls in event.split(','):
            n, color = balls.split()
            n = int(n)
            V[color] = max(V[color],n)
            if int (n) > {'red':12,'green':13,'blue':14}.get(color,0):
               ok = False
        score = 1
        for v in V .values():
            score *= v
        p2 += score
        if ok:
            p1 += int(id_.split()[-1])
print(p1)
print(p2)

result = 0
for line in content.split('\n'):
    ok = True
    id_ ,line = line.split(':')
    for event in line.split(';'):
        for balls in event.split(','):
            n, color = balls.split()
            if int(n) > {'red':12,'green':13,'blue':14}.get(color,0):
               ok = False
    if ok:
        result += int(id_.split()[-1])
        print(id_)
print(result)
"""
 
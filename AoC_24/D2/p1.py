input = open('AoC_24/D2/input.txt').read().splitlines()

def asc (line):
    checked = True
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]
        if line[i] > line[i + 1] or diff < 1 or diff > 3:
           checked = False
           break
    return checked

def desc (line):
    checked = True
    for i in range(len(line) - 1):
        diff = line[i] - line[i+1]
        if line[i] < line[i + 1] or diff < 1 or diff > 3:
           checked = False
           break
    return checked

count = 0
for line in input:
    line = list(map(int, line.split()))
    if asc(line):
        count += 1
    elif desc(line):
        count += 1

print(count)
    



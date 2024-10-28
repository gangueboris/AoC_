# 5:06 - 5:39
input = open('AoC_22/D6/input.txt').read()

def solve(input):
    l = 0
    for r in range(3, len(input)):
        checked = set()
        for k in range(l, r+1):
            if input[k] not in checked:
                checked.add(input[k])
            else:
                break
            if len(checked) == 4:
                return r +1
        l += 1
print(solve(input))
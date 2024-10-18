dataset = open('Day_9/input.txt', 'r').read().splitlines()
dataset = [list(map(int, line.split())) for line in dataset]

def solve(curr):
    if all(x == 0 for x in curr):
        return curr[-1]
    temp = []
    for i in range(len(curr) - 1):
        temp.append(curr[i+1] - curr[i])
    return curr[-1] + solve(temp)


ans = 0
for line in dataset:
    ans += solve(line)

print(ans) # 1974232246

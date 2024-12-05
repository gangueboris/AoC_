from collections import defaultdict
orders, rules = open('AoC_24\D5\input.txt').read().split('\n\n')

ans = 0
process_orders = defaultdict(list)
for line in orders.splitlines():
    a, b = list(map(int,line.split('|')))
    process_orders[a].append(b)

for line in rules.splitlines():
    rule = list(map(int, line.split(',')))
    isValid = True
    for i in range(len(rule)):
        for j in range(i + 1, len(rule)):
            if rule[j] not in process_orders[rule[i]]:
                isValid = False
                break
        if not isValid:
           break
    if isValid:
        index = len(rule) // 2
        ans += rule[index]
          
print(ans)
    
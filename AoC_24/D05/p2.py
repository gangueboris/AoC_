from collections import defaultdict, deque
orders, rules = open('AoC_24\D5\input.txt').read().split('\n\n')

ans = 0
process_orders = defaultdict(list)

for line in orders.splitlines():
    a, b = list(map(int,line.split('|')))
    process_orders[a].append(b)

for line in rules.splitlines():
    rule = deque(list(map(int, line.split(','))))
    isValid = True
    for i in range(len(rule)):
        for j in range(i + 1, len(rule)):
            if rule[j] not in process_orders[rule[i]]:
                isValid = False
                break
        if not isValid:
           break     
    if not isValid:
        temp = []
        while len(rule) > 1:
            n = rule.popleft()
            isCorrect = True
            for k in range(len(rule)):
                if rule[k] not in process_orders[n]:
                    rule.append(n)
                    isCorrect = False
                    break
            if isCorrect:
                temp.append(n)
        temp.append(rule[0])
            
        index = len(temp) // 2
        ans += temp[index]
          
print(ans)

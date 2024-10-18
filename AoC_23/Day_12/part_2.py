# This part2 required using memoizing to not making the same computation over and over again

def isValid(record, start, end):
    if start - 1 < 0 or end + 1 >= len(record):
        return False
    
    if record[start - 1] == '#' or record[end + 1] == '#': # tcheck if the substring is not surrounded by order damage spring
        return False
    
    if '#' in record[:start]: 
        return False
    
    if '.' in record[start:end+1]: # only ? or #
        return False
   
    return True

memo = dict()
def dfs(record, rule):
    # Base case 
    if (record, rule) in memo:
        return memo[(record, rule)]
    if not rule:
        return 0 if '#' in record else 1
    
    count = 0
    for end in range(len(record)):
        start = end - (rule[0] - 1) # take the size range of the nb

        if isValid(record, start, end):
            count += dfs(record[end + 1:], rule[1:])

    memo[(record, rule)] = count
    return count

def unfold(spring, criteria):
    new_spring = ""
    for i in range(4):
        new_spring += str(spring + '?')
    new_spring += spring

    new_criteria = ""
    for i in range(4):
        new_criteria += str(criteria + ',')
    new_criteria += criteria

    return new_spring, new_criteria



ans = 0

for line in open('Day_12/input.txt', 'r').read().splitlines():
    spring, criteria = line.split()
    spring, criteria = unfold(spring, criteria)
    spring = '.' + spring + '.'
    criteria = tuple(map(int, criteria.split(',')))
    ans += dfs(spring, criteria)

print(ans) # 4232520187524
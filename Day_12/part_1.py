# figure out how many different arrangements of operational and broken springs fit the given criteria in each row.
# This is a nonogram problem
"""
Goal: Return sum of nb of arrangements of damage spring can be made in a spring following the rule
Understanding: The idea here is to take a 'substrings' of string and 'size curr_nb_of_damage_spring' and tcheck if we can find # inside of it.
(isvalid function: return true when the substring contains only # or ? and not surrounded by #)
This is the main idea, now to deal with find nb of arrangements, we can use here a dfs.

Because I know that I will use dfs to solve this problem based on the rule so my base can will be ...
"""
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


def dfs(record, rule):
    # Base case 
    if not rule:
        return 0 if '#' in record else 1
    
    count = 0
 
    for end in range(len(record)):
        start = end - (rule[0] - 1) # take the size range of the nb

        if isValid(record, start, end):
            count += dfs(record[end + 1:], rule[1:])

    return count


ans = 0

for line in open('Day_12/input.txt', 'r').read().splitlines():
    spring, criteria = line.split()
    spring = '.' + spring + '.'
    criteria = tuple(map(int, criteria.split(',')))
    ans += dfs(spring, criteria)

print(ans) # 8075

"""
def count_options(springs: str, blocks: Tuple[int]) -> int:
    if not springs:
        if not blocks:
            return 1
        return 0

    if springs[0] == ".":
        return count_options(springs[1:], blocks)

    if springs[0] == "#":
        if not blocks:
            return 0
        if len(springs) < blocks[0]:
            return 0

        for i in range(blocks[0]):
            if springs[i] == ".":
                return 0

        if len(springs) == blocks[0]:
            return count_options("", blocks[1:])
        if springs[blocks[0]] == "#":
            return 0
        return count_options(springs[blocks[0] + 1 :], blocks[1:])

    operational_options = count_options("." + springs[1:], blocks)
    damaged_options = count_options("#" + springs[1:], blocks)
    return operational_options + damaged_options

"""
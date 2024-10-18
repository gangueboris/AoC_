from collections import defaultdict
from functools import cmp_to_key

# This problem is about sorting
# NOTE: Here I would like to compare 5 things(more than 2) so I will return value based on there value
# 
cards = [tuple(line.split()) for line in open('in.txt').read().splitlines()]

def findType(v):
    values = defaultdict(int)
    joker = 0
    for c in v:
        if c == 'J':
            joker += 1
        else:
            values[c] += 1
    count = sorted(values.values())
    if count[-1] + joker == 5:
       return 7
    if count[-1] + joker == 4:
       return 6
    if count[-1] + joker == 3:
        if values == [1, 1, 2]:
            return 4
        return 5
    if count[-1] + joker == 2:
        if values == [1,1,1,1]:
            return 2
        return 3
    return 1

  
def compare(a, b):
    strengh = "AKQT98765432J"
    A = findType(a)
    B = findType(b)
    if A > B:
        return 1
    elif A < B:
        return -1
    else:
        for e, f in zip(a, b):
            if strengh.index(e) < strengh.index(f):
                return 1
            else:
                return -1
        return 0

cards.sort(key= cmp_to_key(lambda x, y: compare(x[0], y[0])))

ans = 0

for i, (_, n) in enumerate(cards, 1):
    ans += i * int(n)
print(ans)           
           

              

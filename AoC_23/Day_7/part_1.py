from collections import Counter
from functools import cmp_to_key

# This problem is about sorting
# NOTE: Here I would like to compare 5 things(more than 2) so I will return value based on there value

cards = [tuple(line.split()) for line in open('in.txt').read().splitlines()]

def findType(v):
    values = sorted(Counter(v).values())
    if 5 in values:
       return 7
    if 4 in values:
       return 6
    if 3 in values:
        if values == [1, 1, 3]:
            return 4
        return 5
    if 2 in values:
        if values == [1,1,1,2]:
            return 2
        return 3
    return 1

def compare(a, b):
    strengh = "AKQJT98765432"
    A = findType(a)
    B = findType(b)
    if A > B:
        return 1
    elif A < B:
        return -1
    else:
        for i in range(len(a)):
            if strengh.index(a[i]) < strengh.index(b[i]):
                return 1
            else:
                return -1
        return 0

cards.sort(key= cmp_to_key(lambda x, y: compare(x[0], y[0])))

ans = 0

for i, (_, n) in enumerate(cards, 1):
    ans += i * int(n)
print(ans)           
           

              

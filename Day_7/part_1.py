"""
Intuition: Sort the hands based on the rule and take their indices as the rank.
Goal: mutiply rank of each hand with there corresponding rid and sum up all result and return it.
NOTE: 
- We have two level of sorting. The first one is 'sorting by type' and the second one is 'sorting by label'.
 
"""

from collections import defaultdict
from functools import cmp_to_key

content = open('Day_7/input.txt', 'r').read().splitlines()
inputs = []
for input in content:
    hand, bid = input.split()
    inputs.append((hand, int(bid)))

def find_type(hand):
    counts = defaultdict(int)
    for c in hand:
        counts[c] += 1
        
    amounts = sorted(counts.values())
    
    if 5 in amounts:
        return 7
    elif 4 in amounts:
        return 6
    elif 3 in amounts:
        if amounts == [1, 1, 3]:
            return 4  # Three of kind
        return 5  # Full house
    elif 2 in amounts:
        if amounts == [1, 2, 2]:
            return 3  # Two pair
        return 2  # One pair
    return 1 # high card
    


def compare(a, b):
    labels = "AKQJT98765432" # strongest to weakest
    
    A = (find_type(a), a)
    B = (find_type(b), b)

    if A[0] > B[0]:
        return 1
    elif A[0] < B[0]:
        return -1
    else:
        for c1, c2 in zip(A[1], B[1]):
            if labels.index(c1) > labels.index(c2):
                return -1
            elif labels.index(c1) < labels.index(c2):
                return 1
        return 0 # Means both are identic




inputs = sorted(inputs, key = cmp_to_key(lambda x,y: compare(x[0], y[0])))

ans = 0
for i, (hand, bid) in enumerate(inputs, 1):
    ans += i * bid

print(ans)  # 249726565

    


    


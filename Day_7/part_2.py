"""
Intuition: Sort the hands based on the rule and take their indices as the rank.
Goal: mutiply rank of each hand with there corresponding rid and sum up all result and return it.
NOTE: 
- J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.
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
    jokers = 0
    for x in hand:
        if x == "J":
            jokers += 1
        else:
            counts[x] += 1

    amounts = sorted(counts.values())
    if jokers >= 5 or amounts[-1] + jokers >= 5:
        return 7
    if jokers >= 4 or amounts[-1] + jokers >= 4:
        return 6

    # Try a full house
    if amounts[-1] + jokers >= 3:
        rem_jokers = amounts[-1] + jokers - 3
        if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 5
        return 4

    if amounts[-1] + jokers >= 2:
        rem_jokers = amounts[-1] + jokers - 2
        if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 3
        return 2
    return 1
    


def compare(a, b):
    labels = "AKQT98765432J" # strongest to weakest
    
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

inputs.sort(key = cmp_to_key(lambda x, y: compare(x[0], y[0])))

ans = 0
for i, (hand, bid) in enumerate(inputs, 1):
    ans += i * bid

print(ans)  # 251135960 

content = open("Day_4/input.txt", 'r').read().splitlines()
"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

An instance card: is
Goal: Sum up the instances cards and return the result.
If we remark well, we have a cumulative operation over here
"""

def totalInstances(content):
    temp = {i:1 for i in range(len(content))} # handle original copy

    for i, line in enumerate(content):
        count = 0
        winning, mine = line.split(':')[1].split('|')
        winning = winning.split()
        mine = mine.split()
        for v in mine:
            if v in winning:
                count += 1
    
        for j in range(count):
            temp[i+j+1] += temp[i]

    return sum(temp.values())
          
print(totalInstances(content)) #  6227972
 

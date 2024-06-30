content = open("Day_4/text.txt", 'r').read().splitlines()
"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

An instance card: is
Goal: Sum up the instances cards and return the result.
"""

def totalInstances(content):
    temp = {i:0 for i in range(1, len(content)+1)}
    for line in content:
        count = 0
        card, numbers = line.split(':')
        _, n = card.split()
        winning, mine = numbers.split('|')
        winning = winning.split()
        mine = mine.split()
        for v in mine:
            if v in winning:
                count += 1
        
        num = [str(c) for c in range(int(n)+1, count+2)]
        print(num)
        
    
totalInstances(content)
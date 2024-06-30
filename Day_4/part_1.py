content = open("Day_4/input.txt", 'r').read().splitlines()

"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

Match number: is a number in my list number which is include in the winning numbers.
Goal: In each game, I must find the match number, calculate the point, sum up point in each game and return the result.

Approch:
res = 0
for each line:
    point = 0
    winning, mine = line.split()
    for v in mine:
       if v in winning:
          if not point:
            point += 1
          else:
             point *= 2 
    res += point
return res
       
    
"""
def totalPoints(content):
    res = 0
    for line in content:
        point = 0
        card, numbers = line.split(':')
        winning, mine = numbers.split('|')
        winning = winning.split()
        mine = mine.split()
        for v in mine:
            if v in winning:
                if not point:
                    point += 1
                else:
                    point *= 2
        res += point
    return res

print(totalPoints(content)) # 26426
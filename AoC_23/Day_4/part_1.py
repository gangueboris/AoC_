# Thsi problem is about cumulative sum
ans = 0
for line in open('in.txt').read().splitlines():
    _, numbers = line.split(':')
    winning, mine = numbers.split('|')
    winning = winning.split()
    mine = mine.split()
    total = 1
    match = 0
    for n in mine:
        if n in winning:
           match += 1
           if match >= 2:
               total *= 2

    ans += total if match else 0

print(ans)
 
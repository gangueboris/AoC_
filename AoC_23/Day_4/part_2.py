content = open("Day_4/input.txt", 'r').read().splitlines()


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
 

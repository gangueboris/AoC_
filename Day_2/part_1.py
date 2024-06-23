with open('Day_2/input.txt', 'r') as file:
    content = file.read().splitlines()

"""
Determine which games would have been possible if the bag had been loaded with only 12 red cubes,
 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

Approch: Count on each line nr of red, nb of blue and ng of green.
if nr <= 12 and nb <= 14 and ng <= 13:
res += id

Have learn:
- slicing
- spliting
return res

Difficulty: to split for counting ?!


Game 74: 5 red, 1 green; 1 blue, 5 red; 8 red, 3 blue

"""
def sumOfIds (content):
    res = 0
    for line in content:
        uniqueColorsContainer = []
        nr, nb, ng = 0, 0, 0
        game, colors = line.split(':')
        subColors = colors.split(';') # [' 2 blue, 10 green', ' 10 green, 14 red', ' 3 green, 5 red, 2 blue', ' 1 red, 3 blue, 7 green', ' 1 blue, 7 red']
        # split with ','
        for part in subColors:
           for u in part.split(','):
                uniqueColorsContainer.append(u.strip())
                
        for ncolor in uniqueColorsContainer:
            if 'red' in ncolor:
                nr += int(ncolor[0:len(ncolor)-len('red')]) # because of space I don't need to write +1
            elif 'blue' in ncolor:
                nb += int(ncolor[0:len(ncolor)-len('blue')])
            elif 'green' in ncolor:
                ng += int(ncolor[0:len(ncolor)-len('green')])

        if nr <= 12 and nb <= 14 and ng <= 13:
            _, id = game.split()
            res += int(id)
    return res

                
    

      
print(sumOfIds(content))

with open('Day_2/input.txt', 'r') as file:
    content = file.read().splitlines()

"""
Approch: Count on each line nr of red, nb of blue and ng of green.
if nr <= 12 and nb <= 14 and ng <= 13:
res += id

Game 74: 5 red, 1 green; 1 blue, 5 red; 8 red, 3 blue
"""
def sumOfIds (content):
    res = 0
    for line in content:
        game, prints = line.split(':')
        parts = prints.split(';')
        validToAdd = True
        for part in parts:
            ncolors = part.split(',')
            for ncolor in ncolors:
                _, n, color = ncolor.split(" ")
                n = int(n)
                if int(n) > {'red': 12, 'blue':14, 'green':13}.get(color, 0):
                    validToAdd = False
                    break
        if validToAdd:
            _, id = game.split(" ")
            res += int(id)
    return res
              
              
        
   
    


      
print(sumOfIds(content))

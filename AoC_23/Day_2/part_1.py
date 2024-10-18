with open('Day_2/input.txt', 'r') as file:
    content = file.read().splitlines()

"""
NOTE: Thsi problem is about knowing how to split text.
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

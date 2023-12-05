result,score = 0, 0
with open("Doc&images\input_day2.txt","r") as file:
    content = file.read()
for line in content.split('\n'):
    digits = []
    for i , c in enumerate(line):
        if c.isdigit(): # Verifier si le tout premier char de line est un int 
            digits.append(c)
        for d,l in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(l): # startwith verifie dans la séquence(line[i:]) si la valeur l débute la séquence
                digits.append(str(d+1)) # Car on passe de l'index au reel
    score = int(digits[0] + digits[-1])
    result += score

print(result)
        

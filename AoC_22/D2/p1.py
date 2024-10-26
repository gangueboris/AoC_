res = 0
for line in  open("AoC_22/D2/input.txt").read().splitlines():
    a, b = line.split()
    if b == 'X':
        res += 1
    elif b == 'Y':
        res += 2
    elif b == 'Z':
        res += 3
    
    if (a == 'A' and b == 'X') or (a == 'B' and b == 'Y') or (a == 'C' and b == 'Z'):
        res += 3 
    elif b == 'X' and a == 'C':
        res += 6
    elif b == 'Y' and a == 'A':
        res += 6
    elif b == 'Z' and a == 'B':
        res += 6
    
   
print(res)
    


  
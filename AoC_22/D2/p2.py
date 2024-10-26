opp = {'A': 'Z', 'B': 'X', 'C': 'Y'}
equal = {'A': 'X', 'B': 'Y', 'C': 'Z'} 
win = {'A': 'Y', 'B': 'Z', 'C': 'X'}

def cal(b):
    res = 0
    if b == 'X':
       res += 1
    elif b == 'Y':
        res += 2
    elif b == 'Z':
        res += 3
    return res
    
ans = 0   
for line in  open("AoC_22/D2/input.txt").read().splitlines():
    a, b = line.split()
    if b == 'X':
        ans += cal(opp[a])
    elif b == 'Y':
        ans += (cal(equal[a]) + 3)
    else:
        ans += (cal(win[a]) + 6)

print(ans)
    


  
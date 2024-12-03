input = open('AoC_24\D3\input.txt').read()

def isValid(s):
    
    for c in s:
        if not c.isdigit():
            return False
    return True

total = 0
for i, c in enumerate(input):
    if c == 'm':
        l = i
        r = l + 1
        while input[r] != ')':
            r += 1
        mul = input[l+3:r+1]
        if mul.startswith('('):
            mul = mul.split(',')
            try:
                if len(mul) == 2 and isValid(mul[0][1:]) and isValid(mul[1][:-1]):
                    total += int(mul[0][1:]) * int(mul[1][:-1])
            except ValueError as e:
                print(mul)
                print("ValueError:", e)

       
print(total)
            
        
        

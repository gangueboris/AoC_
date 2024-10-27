#7:30 : 8:03 8: 21
input = open('AoC_22/D3/input.txt').read().splitlines()
res = 0

for i in range(2,len(input), 3):
    first, second, third = input[i-2], input[i-1], input[i]
    checked = set()
    for c in first:
        if c in second and c in third and c not in checked:
            if c.islower():
                res += ord(c) - 96
            else:
                res += ord(c) - 38
            checked.add(c)  
print(res)  
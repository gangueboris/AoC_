with open("Day_1\p1.txt", 'r') as file:
    content = file.read().splitlines()
    
"""
Approch: store all digits or digitsChar that we can find and take the first and the last
"""
def findCode2(content):
    res = 0
    digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4 , 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for line in content:
        temp = []
        for id, char in enumerate(line):
            if char.isdigit():
                temp.append(char)
            for v,i in digits.items():
                if line[id:].startswith(v):
                    temp.append(str(i))
        res += int(temp[0]+temp[-1])
    return res

print(findCode2(content))
                
                


               
            




      
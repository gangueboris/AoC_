with open("Doc&images\input_day1.txt","r") as file:
    content = file.read()
 
score, result = 0,0
for line in content.split('\n'):
    digits = []
    for c in line:
       if c.isdigit():
          digits.append(c)
    score = int(digits[0] + digits[-1])
    result+= score
print(result)

    

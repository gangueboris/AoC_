with open("Day_4\data.txt",'r') as file:
    content = file.read()

content = content.split("\n")

cards = [content[i].split(':')[0] for i in range(len(content))]
others = [content[i].split(':')[1] for i in range(len(content))]
wins = [[c for c in others[i].split('|')[0].split()] for i in range(len(others))]
data = [[c for c in others[i].split('|')[1].split()] for i in range(len(others))]

result = 0
for i, j in zip(data,wins):  
    point = 0
    for w in i: 
        if w in j:
           if point<1:  
              point += 1
           else:
              point *= 2
    result += point      
   
print(result)
    

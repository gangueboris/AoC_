with open("Day_4\Doc&images\data.txt",'r') as file:
    content = file.read()

content = content.split("\n")

cards = [content[i].split(':')[0] for i in range(len(content))]
others = [content[i].split(':')[1] for i in range(len(content))]
wins = [[c for c in others[i].split('|')[0].split()] for i in range(len(others))]
datas = [[c for c in others[i].split('|')[1].split()] for i in range(len(others))]

result = 0
"""
for data, win in zip(datas,wins):  
    point = 0
    for d in data: 
        if d in win:
           if point < 1:  
              point += 1
           else:
              point *= 2
    result += point      
   
print(result)
"""
for data, win in zip(datas,wins):  
    point = 0
    for d in data: 
        if d in win:
           point += 1
    if point > 0:    
      result += 2**(point - 1)
print(result)
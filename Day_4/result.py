with open("Day_4\data.txt",'r') as file:
    content = file.read()

content = content.split("\n")

cards = [content[i].split(':')[0] for i in range(len(content))]
others = [content[i].split(':')[1] for i in range(len(content))]
wins = [others[i].split('|')[0] for i in range(len(others))]
data = [others[i].split('|')[1] for i in range(len(others))]


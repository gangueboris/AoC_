import numpy as np

with open("Day3/test.txt", 'r') as file:
    content = file.read()

# Creation de DFS
visited_list = []

def DFS(graph, i, j, visited_list):
    if 0 <= i < graph.shape[0] and 0 <= j < graph.shape[1] and (i, j) not in visited_list and graph[i][j] != '.':
        visited_list.append((i, j))
        for (neiX, neiY) in [(i, j), (i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), (i - 1, j - 1), (i + 1, j + 1),
                             (i - 1, j + 1), (i + 1, j - 1)]:
            DFS(graph, neiX, neiY, visited_list)

result = 0
temp = 0
a,b = 0,0
graph = []

for line in content.split('\n'):
    char = []
    for c in line:
        char.append(c)
    graph.append(char)

graph = np.array(graph)

for i in range(graph.shape[0]):
    digit = '0'
    for j in range(graph.shape[1]):
        if graph[i][j].isdigit():
            digit += graph[i][j]
        else:
            temp = int(digit)
            a, b = str(temp)[0],str(temp)[-1]
            for (k,l) in [()]
           
            print(temp)
    #digit = int(digit)
    #rint(digit)
    #result += digit

#print(result)








print(a,b)







"""
for line in content.split('\n'):
    digit = '0'
    for i in len(line):
        temp += 1
        if temp < len(line):
            for j in len(line):
                if i.isdigit():
                    digit += i
                    DFS(content,i,j,line)


                else :
                    digit = '0'
                    
"""
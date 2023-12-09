import numpy as np
with open("Day3/test.txt", 'r') as file:
     content = file.read()
#print(content)

#graph = [[c for c in line] for line in content.split('\n')]

def identification(content):
    position = []
    nbres = []
    for i,line in enumerate(content.split('\n')):
        tempPos = []
        tempNb = []
        for j ,c in enumerate(line):
            if c.isdigit():
                tempNb.append(c)
                tempPos.append((i,j))
            else:
                if tempNb != []:
                   position.append(tempPos)
                   nbres.append(tempNb)
                tempPos = []
                tempNb = []
    return position,nbres     

position,nbres = identification(content)

graph = np.array([[c for c in line] for line in content.split('\n')])

def parcours(graph,position ,nbres):
    for nb,ps in zip(nbres,position):
        result = 0
        if len(nb) == 3:
            k,l = ps[1][0],ps[1][1]
            #graph[k][l]
            if 
            for nx,ny in [(k+2,l),(k-2,l),(k,l+1),(k,l-1),(k+1,l+1),(k+1,l-1),(k+2,l+1),(k+2,l-1),(k-1,l+1),(k-1,l-1),(k-2,l+1),(k-2,l-1)]:
                if graph[nx][ny] !='.' and graph[nx][ny].isdigit() == False:
                    nb = int(nb)
                    result += nb


parcours(graph,position,nbres)
        

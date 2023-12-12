import numpy as np
with open("Day3\part1.txt", 'r') as file:
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
    result = 0
    for nb,ps in zip(nbres,position):
        if len(nb) == 3:
            k,l = ps[1][0],ps[1][1]
            for (nx,ny) in [(k,l+2),(k-1,l+2),(k-1,l+1),(k-1,l-1),(k-1,l-2),(k,l-2),(k+1,l-2),(k+1,l-1),(k+1,l),(k+1,l+2),(k-1,l),(k+1,l+1)]:
                if 0<= nx < graph.shape[0] and 0 <= ny < graph.shape[1] and graph[nx][ny] !='.' and not graph[nx][ny].isdigit():
                   nbre = int(graph[k][l-1] + graph[k][l] + graph[k][l+1])
                   result += nbre
        elif len(nb) == 2:
            k,l = ps[1][0],ps[1][1]
            for (nx,ny) in [(k,l+1),(k-1,l+1),(k-1,l),(k-1,l-1),(k-1,l-2),(k,l-2),(k+1,l-2),(k+1,l-1),(k+1,l),(k+1,l+1)]:
                if 0<= nx < graph.shape[0] and 0<= ny < graph.shape[1] and graph[nx][ny] !='.' and not graph[nx][ny].isdigit():
                    nbre = int(graph[k][l-1]+graph[k][l])
                    result += nbre
        elif len(nb) == 1:
            k,l = ps[0][0],ps[0][1]
            #print(nb)
            for (nx,ny) in [(k,l+1),(k-1,l+1),(k-1,l),(k-1,l-1),(k,l-1),(k+1,l-1),(k+1,l),(k+1,l+1)]:
                if 0<= nx < graph.shape[0] and 0<= ny < graph.shape[1] and graph[nx][ny] !='.' and not graph[nx][ny].isdigit():
                    nbre = int(graph[k][l])
                    #print(nbre)
                    result += nbre
       
    return result

res = parcours(graph,position,nbres)
print(res)

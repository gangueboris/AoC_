with open("Doc&images\input_day2.txt","r") as file:
    file = file.read()

letterList = ["one","two","three","four","five","six","seven","eight","nine"]
digitList = [0,1,2,3,4,5,6,7,8,9]


lines = file.split("\n")
index = 0 
count = 0
digitIndex = 0
for line in lines:
    if line not in lines:
        continue
    for i in range(len(letterList)):
        while index < len(line):
            index = line.find(letterList[i],index) # la methode find me renvoi -1 si le sous-charactere n'a pas été trouvé
            if index == -1: break   
            count += 1
            digitIndex = i
            index += 1 # Pour continue la recherche à partir du charactere suivant sinon l'algo va repeter la même chose
        count = 0    
      

import numpy as np
with open("Doc&images\input_day1.txt","r") as file:
    file = file.read()

lines = file.split("\n")
charList = []
for line in lines:
    if line not in lines:
        continue  
    digits = tuple(int(char) for char in line if char.isdigit())
    charList.append(digits)

newList = []
for digits in charList:
    lenDigits = len(digits)
    first = digits[0]
    last = digits[lenDigits-1]
    digit = str(first) + str(last)
    digit = int(digit)
    newList.append(digit)


result = np.sum(newList) # result = 53921
print(result) 
    

import numpy as np

input = open('Debit_Tableau_Evan_Boris.csv').read().splitlines()
temps, W, Uq = [], [], []
for line in input[1:]:
    t, w, uq = line.split(';')
    temps.append(float(t))
    W.append(float(w))
    Uq.append(float(uq))
print(temps)

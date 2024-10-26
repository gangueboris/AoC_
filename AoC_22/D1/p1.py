#9:48 : 9:52 solve at 10:01
import numpy as np
ans = 0
for calories in  open("AoC_22/D1/input.txt").read().split("\n\n"):
    cals = calories.split()
    cals = [int(c) for c in cals]
    ans = max(ans, np.sum(cals))
print(ans)
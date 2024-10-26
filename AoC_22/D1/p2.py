#9:48 : 9:52 solve at 10:01 p2 at 10:5
import numpy as np
ans = []
for calories in  open("AoC_22/D1/input.txt").read().split("\n\n"):
    ans.append(np.sum([int(c) for c in calories.split()]))
ans.sort(reverse=True)

print(ans[0] + ans[1] + ans[2])
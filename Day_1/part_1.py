"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration
value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit 
and the last digit (in that order) to form a single two-digit number.
"""


with open('Day_1\p1.txt', 'r') as file:
   content = file.read().splitlines()

def findCode(content):
    res = 0
    for line in content:
      Findfirst = True
      for c in line:
        if c.isdigit() and Findfirst:
           first= c
           Findfirst = False
        if c.isdigit():
           last = c
      res += int(first+last)
    return res

print(findCode(content))    
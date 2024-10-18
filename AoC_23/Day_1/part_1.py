"""
NOTE: regex: We are using the regrex to find the a word, substring, digit, number in a string.
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
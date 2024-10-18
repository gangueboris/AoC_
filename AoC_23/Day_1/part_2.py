import re
ans = 0
maps = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
pattern = '|'.join(number_words) + '|\d'

for line in open("in.txt").read().splitlines():
    output = re.findall(pattern, line)
    ans += int(str(maps.get(output[0], output[0])) + str(maps.get(output[-1], output[-1])))

print(ans)
               
            




      
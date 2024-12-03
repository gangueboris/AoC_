import re

input = open('AoC_24\D3\input.txt').read()

total = 0
enabled = True  

mul = re.compile(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
state = re.compile(r"(do\(\)|don't\(\))")

i = 0
while i < len(input):

    state_match = state.match(input, i)
    if state_match:
        if state_match.group() == "do()":
            enabled = True
        elif state_match.group() == "don't()":
            enabled = False
        i += len(state_match.group())
        continue
    mul_match = mul.match(input, i)
    if mul_match and enabled:
        x, y = map(int, mul_match.groups())
        total += x * y
        i += len(mul_match.group())
        continue

    i += 1

print(total)

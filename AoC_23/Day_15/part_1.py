seq = open('Day_15/input.txt', 'r').read().split(',')
# This day_15 problem's is about implementing a hash function.
# NOTE: How to find the ascii code in any programming language ?

def hash(s):
    res = 0
    for c in s:
        res += ord(c)
        res *= 17
        res %= 256
    return res

ans = 0
for s in seq:
    ans += hash(s)

print(ans) # 514281
    
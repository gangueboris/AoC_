"""
Multi-step mapping problem or transitive mapping problem, where you need to convert one category to another
through a series of intermediate categories, using a set of mappings
"""
seeds, *mapping = open('in.txt').read().split('\n\n')
seeds = list(map(int, seeds.split(':')[1].split()))
ans = 99999999999999
for seed in seeds:
    curr = seed
    for maps in mapping:
        for line in maps.split('\n')[1:]:
           dest, src, steps = list(map(int, line.split()))
           if src <= curr <= src + steps:
               curr = dest + (curr - src)
               break
    ans = min(ans, curr)

print(ans)
    
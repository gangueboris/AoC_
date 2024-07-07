"""
Note: In this part2, seeds are now put by pairs to form range of seeds. But the questions remains the same; find the min location.
The difficulty here is that, we have range, range of billions seeds to handle.

Intuition: We can handle ranges by using interval with overlapping.

Approch: 
- seeds = list of pairs(start, end) seeds.
- Go map by map
- Find overlaps between seeds(start, length) and the source range(src, src + rang). Let's not forget to manage the remains seeds and seeds which are
themselves src & dest.
- find min and return.
"""

input, *blocks = open('Day_5/input.txt', 'r').read().split('\n\n')

#extract and convert seeds to int
input = list(map(int, input.split(':')[1].split()))

# Form pairs (start, end)
seeds = [(input[i], input[i] + input[i+1]) for i in range(0, len(input), 2)]

for block in blocks:
    ranges = []                                              # Store numbers of each map
    for numbers in block.split('\n')[1::]:
        ranges.append(list(map(int, numbers.split())))

    new_seed = []
    while seeds:
        start, end = seeds.pop()
        for dest, src, rang in ranges:                           # Go numbers by numbers in each map
            os = max(start, src)
            oe = min(end, src + rang)
            if os < oe:                                                 # Be sure that we find the overlap
                new_seed.append((dest + os - src, dest + oe - src))    # Add all dest as range to new_seed
                # Manage remains
                if start < os:   # check left if remains
                    seeds.append((start, os))
                if oe < end:       # check right if remains
                    seeds.append((oe, end))
                break        
        else:
            new_seed.append((start, end))                # Add out of overlap to the new_seed (seeds which are src == dest) for the next map
    seeds = new_seed                                     # update the seed for the next map
   
print(min(seeds)[0]) # 1240035

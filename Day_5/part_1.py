"""
The first line has a destination range start of 50, a source range start of 98, and a range length of 2.

Goal: find the minimum location value for a seed.
approch: for each seed, browse the map until I reach the location.

Approch1: 
- For each seed, browse the entire blocks to reach the location and store it.
- Find the min of locations and return it.

Question: How to make the dest of one category to the start of the next until I reach the location
I need something to reset the count in the loop, something like separator


Approch2:
** We remark that each level in the map has and input list (for the first, the seed list and other ther output of the previous level)
- Find for each seed the dest in the current category before moving to the next
- The last level contains (the last mapping) the answers that we are looking for.

"""
#---------------------------------- Approch 2 --------------------------------------------#
seeds, *blocks = open('Day_5/test.txt', 'r').read().split('\n\n')
def approch_one(seeds, blocks):
    seeds = list(map(int,seeds.split(':')[1].split()))

    for block in blocks:
        ranges = []
        for numbers in block.split('\n')[1::]:
            ranges.append(list(map(int, numbers.split())))
        new_seed = []
        for seed in seeds:
            for dest, src, rang in ranges:
                if src <= seed < src + rang:
                    new_seed.append(dest + (seed - src))
                    break
            else:
                new_seed.append(seed)
        seeds = new_seed
    return min(new_seed)
print(approch_one(seeds, blocks))

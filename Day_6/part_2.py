time, distance = open('Day_6/input.txt', 'r').read().splitlines()
time = int(''.join(time.split(':')[1].split()))
distance = int(''.join(distance.split(':')[1].split()))

"""
# Optimize approch run on binary search
[0, time]
recordInterval = [a, b]
ans = b - a + 1
How to find the record interval ?
Note: RecordIntervalTime is the interval of time for which each time T give a (time - T) * T > distance
"""
ans = 0
cDistance = 0
cTime = 0
while cTime <= time:
    cDistance = (time - cTime) * cTime #  * cTime = * speed
    if cDistance > distance:
        ans += 1
    cTime += 1
print(ans) #  34655848


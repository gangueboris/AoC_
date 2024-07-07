time, distance = open('Day_6/input.txt', 'r').read().splitlines()

time = list(map(int,time.split(':')[1].split()))
distance = list(map(int,distance.split(':')[1].split()))


"""
(4 * 8 * 9)

"""
ans = 1
for t, d in zip(time, distance):
    cTime = 0
    cDistance = 0
    count = 0
    while cTime <= t:
        cDistance = (t - cTime) * cTime # * cTime = * speed
        cTime += 1
        if cDistance > d:
            count += 1
    ans *= count

print(ans) # 588588

         

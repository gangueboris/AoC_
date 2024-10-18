time, distance = open('in.txt').read().splitlines()
time = list(map(int, time.split(':')[1].split()))
distance = list(map(int, distance.split(':')[1].split()))
ans = 1
for i, t in enumerate(time):
    count = 0
    for n in range(t + 1):
        if n * (t - n) > distance[i]:
            count += 1
    ans *= count

print(ans)



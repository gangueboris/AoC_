time, distance = open('in.txt').read().splitlines()
time = int(''.join(time.split(':')[1].split()))
distance = int(''.join(distance.split(':')[1].split()))

count = 0
for n in range(time + 1):
    if n * (time - n) > distance:
        count += 1
print(count)             
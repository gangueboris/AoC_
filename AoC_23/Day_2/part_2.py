ans = 0
for line in open('in.txt', 'r').read().splitlines():
    _, record = line.split(':')
   
    r, g, b = 0, 0, 0

    for ncolors in record.split(';'):
        for nc in ncolors.split(','):
            n, c = nc.split()
            n = int(n)
            if  c == 'green':
                g = max(g, n)
            if c == 'red':
                r = max(r, n)
            if c == 'blue':
                b = max(b, n)
    ans += r * b * g
          
    
print(ans)
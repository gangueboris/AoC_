plan = [tuple(line.split()) for line in open("Day_18/in.txt", "r").read().splitlines()]
print(sum(list(map(int, list(n[1] for n in plan)))))

# This problem smell flood fill algorithm  (method 1)
# We can be help by using the sheolaces an pick's: which allow us to compute the erea of any polygon given an integer coordonate (method 2)

# In the problem, we have also geometric figure base on the input (cf day10 part 2)
# Approch:   

def drawBord(grid, plan):
    # Plan = [Position, Numbers]
    for line in plan:
        currPosition = line[0]
        n = line[1]
        r, c = (5, 5) #(r, c) of the middle
        while n > 0: #  I suppose that I'm in bound
            if currPosition == 'T': 
                grid[r][c] = '#'
                r -= 1
            
            if currPosition == 'B': 
                grid[r][c] = '#'
                r += 1
            
            if currPosition == 'R': 
                grid[r][c] = '#'
                c += 1
            
            if currPosition == 'L': 
                grid[r][c] = '#'
                c -= 1
            
            n -= 1



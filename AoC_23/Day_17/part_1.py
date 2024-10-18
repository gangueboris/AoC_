# This problem is about finding the shortest path (start - end) and return the sum of the min distance
#To solve this problem, we can use the Djistraski's algorithm; here (queue for DFS && priority queue)
"""
continue moving right while counting the number of steps. if the n_steps == 3 or next_block > curr_block: tcheck condition to turn

if coords == dest:
return ans

** Conditions to turn **
if top is bound and not in visited and < curr:
   add top coord to the queue:

ans = 0
steps = 0
stack = []
visited = set()

while coords != dest:
    curr = stack.pop()
    steps += 1
    if steps != 0:
       ans += 1
    if curr not in visited:
        visited.add(curr)
    
    if steps <= 3 and curr_next inbound and curr_next not in visited:
       stack.add(curr_next)
       continue  # because I'm using here a stack   right

    if steps <= 3 and curr_next inbound and curr_next not in visited:
       stack.add(curr_next)
       continue  # because I'm using here a stack   top

    if steps <= 3 and curr_next inbound and curr_next not in visited:
       stack.add(curr_next)
       continue  # because I'm using here a stack  back
       
    else:
       steps = 0

return ans



       
    
    
    
   
   
     

"""
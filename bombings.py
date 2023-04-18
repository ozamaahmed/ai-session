 
# this function will calculate every single nodes heuristic and return the minimum of them (can be optimized)
def m_heuristic(node,bombs):
    h = [0 for i in range(len(bombs))]
    for i in range(len(bombs)):
        if bombs[i] not in v:
            d = abs(node[0]-bombs[i][0])+abs(node[1]-bombs[i][1])
            h[i] = d+ (bombs[i][3] / (bombs[i][2]**2))
        else:
            h[i] = 999
    small =h.index(min(h))
    # we are returning the index of minimum of the hueristic and the distance of that bomb
    return small,abs(node[0]-bombs[small][0])+abs(node[1]-bombs[small][1])
 
 
 
v = [] # to keep in track what was visited
# the bombs are in the order of x,y,casualties,go off time
bombs = [[3, 5,10,2],[10, 2,12,5],[7, 9,13,7],[1, 8,30,8],[6, 3,25,6],[9, 6,20,14]]
 
#this function will traverse thru each node and call heuristic after each step
def trav(n,bombs):
    v.append(n) # we visit the first bomb as n is the [x,y,c,g] of the first bomb
    way = [n] # first one is added to the way array which represents the path that we go
    node = n[0:2] # this is the x,y of first bomb (we teleport here)
    highest_time = max([i[3] for i in bombs])
    time = 0  # we keep track of how much time is done
    # traversing thru each one by min(heuristic) and appending to the way
    while len(v)<len(bombs) and time<highest_time: 
        # we check every iteration if the time has gone more than the go off times of some bombs we skip the bombs that have been went of by putting them in visited
        for i in range(len(bombs)):
            if bombs[i][3] <= time:
                v.append(bombs[i])
                
        next,d = m_heuristic(node,bombs) # we get returned the next bomb to go next ( its index) based on the heuristic value and its distance from current bomb. 
        way.append(bombs[next]) # we append that to our WAY array
        v.append(bombs[next]) # and then we put it in visit 
        node = way[-1][0:2] # this is the x,y of next bomb
        time+=d+p # we are adding the time it took to travel and diffuse time to the total time over.
        
 
    return way
 
 
#take the input of the time it takes to diffuse one bomb
p = 2
# we are starting to diffuse from the first bomb
print(trav(bombs[0],bombs))


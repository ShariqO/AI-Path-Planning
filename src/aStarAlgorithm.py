"""
-------------------------------------------------------
A* algorithm implementation 
-------------------------------------------------------
-------------------------------------------------------
"""
import math
from spot import spot
def return_path(spot):
    #initialize the path
    path = []
    current = spot
    while current is not None:
        path.append(current.location)
        current = current.prev
    #return the path used
    return path[::-1]

#calculate the h value
def heuristic(neighbor, end):
    distance = ((neighbor.location[0] - end.location[0]) ** 2) + ((neighbor.location[1] - end.location[1]) ** 2)
    #distance = math.sqrt( ((end.location[0]-neighbor.location[0])**2)+((end.location[1]-neighbor.location[1])**2) )
    return distance;

def aStar(grid, start, end):
    #define spot objects to the start and end
    start = spot(None, start)
    end = spot(None, end)
    
    #define open set and closed set for unchecked and checked spots
    openSet = []
    closedSet = []

    #add the start spot into the open set
    openSet.append(start)
    
    count = 0
    max_iterations = (len(grid) // 2) ** 2
    
    #keep going through the open set until you find the end 
    while len(openSet) > 0:
        #increment count
        count += 1
        
        #set the current node to the first node in the open set 
        cur = openSet[0]
        cur_index = 0
        for index, item in enumerate(openSet):
            if item.f < cur.f:
                cur = item
                cur_index = index
        
        #Check for infinite loop in case cant find path
        if count > max_iterations:
            print("Cannot find path")
            return;
        
        #remove the current node from the open set and move it to the closed set
        openSet.pop(cur_index)
        closedSet.append(cur)
    
        #check if it has reached the end goal
        if cur == end:
            #initialize the path
            return return_path(cur)
            
        #initialize neighbors list
        neighbors = []
        #define adjacent spots
        adjacent = ((0, -1), (0, 1), (-1, 0), (1, 0))
        
        for new_location in adjacent: 
            # Get spot location
            spot_location = (cur.location[0] + new_location[0], cur.location[1] + new_location[1])
            
            # Make sure its in the grid
            if spot_location[0] > (len(grid) - 1) or spot_location[0] < 0 or spot_location[1] > (len(grid[len(grid)-1]) -1) or spot_location[1] < 0:
                continue

            # Make sure it is not an obstacle
            if grid[spot_location[0]][spot_location[1]] != 0:
                continue
            
            # Create new spot
            new_spot = spot(cur, spot_location)

            # Append to the neighbors
            neighbors.append(new_spot)

        # Loop through neighbors
        for neighbor in neighbors:

            # neighbor is in the closed list, skip it
            if len([closed for closed in closedSet if closed == neighbor]) > 0:
                continue

            #calculate the f, g, and h values for the spot
            neighbor.g = cur.g + 1
            neighbor.h = heuristic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h

            # check neighbor is already in the open list
            if len([opened for opened in openSet if neighbor == opened and neighbor.g > opened.g]) > 0:
                continue

            # Add the neighbor to the open list
            openSet.append(neighbor)



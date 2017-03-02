import sys
import heapq


class tile:
    val = 0
    added = False
    cleared = False
    tnt_seen = False
    
    def __init__(self, val):
        self.val = val

def print_grid(grid):
    for x in grid:
        print x.val,

def add_tiles(grid, pq, current, size):
    row = current[2]
    col = current[1]
    up = (row-1)*size + col
    down = (row+1)*size + col
    left = row * size + (col-1)
    right = row * size + (col + 1)
    
    if grid[up].added == False:
        grid[up].added = True
        x = (grid[up].val, up % size, up / size) #rubble, col, row
        heapq.heappush(pq, x)
    if grid[down].added == False:
        grid[down].added = True
        x = (grid[down].val, down % size, up / size) #rubble, col, row
        heapq.heappush(pq, x)
    if grid[left].added == False:
        grid[left].added = True
        x = (grid[left].val, left % size, left / size) #rubble, col, row
        heapq.heappush(pq, x)
    if grid[right].added == False:
        grid[right].added = True
        x = (grid[right].val, right % size, right / size) #rubble, col, row
        heapq.heappush(pq, x)

def add_tiles_TNT(grid, pq, current, size):
    row = current[2]
    col = current[1]
    up = (row-1)*size + col
    down = (row+1)*size + col
    left = row * size + (col-1)
    right = row * size + (col + 1)
    
    if row != 0 and not grid[up].cleared and not grid[up].tnt_seen:
        grid[up].tnt_seen = True
        x = (grid[up].val, up % size, up / size)
        heapq.heappush(pq, x)
    if row != size - 1 and not grid[down].cleared and not grid[down].tnt_seen:
        grid[down].tnt_seen = True
        x = (grid[down].val, down % size, down / size)
        heapq.heappush(pq, x)
    if col != 0 and not grid[left].cleared and not grid[left].tnt_seen:
        grid[left].tnt_seen = True
        x = (grid[left].val, left % size, left / size)
        heapq.heappush(pq, x)
    if col != size - 1 and not grid[right].cleared and not grid[right].tnt_seen:
        grid[right].tnt_seen = True
        x = (grid[right].val, right % size, right / size)
        heapq.heappush(pq, x)

def TNT_det(grid, pq, current, size, count, tot):
    
    add_tiles_TNT(grid, pq, current, size)
    
    while pq:
        current = pq[0]
        pos = current[2] * size + current[1]
        grid[pos].tnt_seen = False
        heapq.heappop(pq)
        tile_val = 0
        if not grid[pos].cleared:
            tile_val = grid[pos].val
            grid[pos].cleared = True
        
        if tile_val == -1:
            TNT_det(grid,pq,current,size,count,tot)
        elif tile_val > 0:
            count[0] += 1
            tot[0] += tile_val
#else: do nothing because tile = 0



def main():
    #get essential numbers from the file
    type = raw_input()
    minesize = int(raw_input().split()[1]) #size: 7, grab second elt
    
    temp = raw_input().split()
    rowstart = int(temp[1])
    colstart = int(temp[2])
    
    vals = [] #get all grid values as a list
    
    for x in xrange(minesize):
        a = raw_input().split() #default separator is " " (whitespace) so this is the same as inp[x].split(" ")
        vals += a
    
    grid = [] #make grid of tiles
    for x in vals:
        # grid += tile(x) #why doesn't this work?
        grid.append(tile(int(x)))
    
    current = (grid[rowstart * minesize + colstart].val, colstart, rowstart)
    cleared_count = [0]
    total_rubble = [0]

pq = [] #initialize empty pq (list to be manipulated by heapq functions)
    #pushed to PQ will be a tuple: rubble, col, row
    pos = current[2]*minesize + current[1]
    grid[pos].added = True
    heapq.heappush(pq,current)
    
    while(True):
        
        current = pq[0]
        heapq.heappop(pq)
        add_tiles(grid, pq, current, minesize)
        
        pos = current[2]*minesize + current[1] #grid index
        if grid[pos].cleared == False:
            tile_val = grid[pos].val
            grid[pos].cleared = True
            if tile_val > 0:
                cleared_count[0] += 1
                total_rubble[0] += tile_val
            else:
                q = []
                TNT_det(grid, q, current, minesize, cleared_count, total_rubble)
        #update priorities
        #print current[2], current[1]
        if (current[2] == 0 or current[2] == minesize - 1 or current[1] == 0 or current[1] == minesize - 1):
            break

print "Cleared %d tiles containing %d rubble and escaped." % (cleared_count[0], total_rubble[0])



if __name__ == "__main__":
    main()

#imports

import matplotlib.pyplot as plt
import random as rn
# funcs

def printMaze(grid, size):
    for y in range(size):
        for x in range(size):
            print(grid[y][x]," ",end = "")
            
        print()
        
        
def show_image(grid, size):
    
    img = []
    
    for y in range(size):
        
        line = []
        
        for x in range(size):
            
            if grid[y][x] == "+":
                line.append(1)
            else:
                line.append(0)
                
        img.append(line)
        
  
    plt.imshow(img, cmap = 'binary')
    plt.show()
            
    
    
def loop_generate(y, x, grid, size, k):
    
    progress = 0
    
    q = []
    q.append([y,x])
    
    while(q):
        
        
        # open the closed cell
        grid[q[len(q)-1][0]][q[len(q)-1][1]] = " "
        neighbors = get_neighbors(y, x, grid, size)
        
        
        #show_image(grid,size)
        
        if (not neighbors):
            q.remove(q[len(q)-1])
            
            if(q):
                y, x = q[len(q)-1]
            
            continue
        
        j, i = rn.choice(neighbors)
        
        grid[j][i] = " "
       
        # remove in between wall
        grid[int((y + j) / 2)][int((x + i) / 2)] = " "
        y = j
        x = i
        q.append([j,i])
        
        # progress counter
        
        progress += 1
        print(int(progress/k * 100), "%")
        
        
        
        
        
    
    return grid;
    

def get_neighbors(y, x, grid, size):
    
    neighbors = []
    
    top = y - 2
    right = x + 2
    bot = y + 2
    left = x - 2
    
    if top >= 1:
        if grid[top][x] == "C":
            neighbors.append([top, x])
        
    if right <= size - 2 :
         if grid[y][right] == "C":
            neighbors.append([y, right])
        
    if bot <= size - 2 :
         if grid[bot][x] == "C":
            neighbors.append([bot, x])
        
    if left >= 1 :
         if grid[y][left] == "C":
            neighbors.append([y, left])
    
    
  
    return neighbors
            

######################################################################################
def maze_generate(size):
    # init
    grid = []
    cells = []



    # generating
    # note: size must be odd


    # number of closed cell
    k = 0


    for y in range(size):

        line = []

        # each cell in a grid is labeled as W as wall, C as closed cell, ' ' as open cell or open wall.
        for x in range(size):


            # chessboard algo
            if x % 2 == 0:
                line.append("+")
            elif y % 2 == 0:
                line.append("+")
            else:
                line.append("C")
                k += 1
                cells.append([y, x])

        grid.append(line)



    # starting position

    grid[1][0] = "S"

    # finishing position

    grid[size-1][size-2] = "E"


    cell = rn.choice(cells)

    grid = loop_generate(cell[0],cell[1], grid, size, k)

    # grid[1][5] = " "
    #printMaze(grid,size)

    show_image(grid,size)

    
############################################ MAIN #############################################

#while(True):
    #maze_generate(1)
print("MAZE GENERATION\n")
maze_generate(int(input("**note: use even number\nenter dimension(eg. 12 if you want 12x12): ")) + 1)





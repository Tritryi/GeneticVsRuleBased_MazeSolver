from maze import Maze
import time

mazeObject = Maze()

def executeRigthtHand():
    mazeObject.clear()
    time.sleep(0.3)

    """
    Algorithm to solve the maze : the right hand rule, always heading right. In algorithmic terms :
    on each step:
        (1) is there a wall on the right:
            no :
                turn right
            yes : 
                go to (2)
            
                
        (2) is there a wall in front of me:
            yes : 
                go to (3)
            no :
                make a step in front
                
        (3) is there a wall on the left:
            yes : 
                go backwards (it is a dead-end)
            no : 
                go left
                
    """
    mazeObject.clear()
    mazeObject.printMaze()
    time.sleep(0.3)

    x = mazeObject.getX()
    y = mazeObject.getY()
    maze = mazeObject.getMaze()

    # define directions
    directions = [
        (0, -1), # 0 = North
        (1, 0),  # 1 = East
        (0, 1),  # 2 = South
        (-1, 0), # 3 = West
    ]

    # at the beginning we look to the right (east)
    orientation = 1
    steps = 0

    while x != 3 or y != 0:
        # for example, if orientation = 2, our right is 3 (west)
        right_direction = (orientation+1) % 4
        dx_d, dy_d = directions[right_direction]
        
        right_cell_x = x + dx_d
        right_cell_y = y + dy_d
        
        if maze[right_cell_y][right_cell_x] == 0: # there is a way on the right, i go there
            orientation = right_direction
            x = right_cell_x
            y = right_cell_y
            steps +=1        

            
        else : 
            dx_d, dy_d = directions[orientation]
            cell_infront_x = x + dx_d
            cell_infront_y = y + dy_d
            
            if maze[cell_infront_y][cell_infront_x] == 0: # there is no wall in front of me, i go there
                # orientation does not move
                x = cell_infront_x
                y = cell_infront_y
                steps +=1        

                
            else:
                orientation = (orientation-1) % 4
        mazeObject.updateOrientation(orientation)
        mazeObject.updateX(x)
        mazeObject.updateY(y)
        
        mazeObject.clear()
        mazeObject.printMaze()
        time.sleep(0.3)   

    print(f"Number of steps to resolve the maze : {steps}")
    return steps
        


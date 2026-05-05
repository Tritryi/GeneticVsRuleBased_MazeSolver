from genetic_algorithm import executeGA
from right_hand_rule import executeRigthtHand
from maze import Maze
import numpy as np
import matplotlib.pyplot as plt
import time

mazeObject = Maze()

def printGaMaze(genome):
    mazeObject.clear()
    mazeObject.printMaze()
    time.sleep(0.3)
    directions = [
        (0, -1), # 0 = North
        (1, 0),  # 1 = East
        (0, 1),  # 2 = South
        (-1, 0), # 3 = West
    ]
    x= mazeObject.getX()
    y= mazeObject.getY()
    orientation=1
    maze = mazeObject.getMaze()
    for move in genome:
        dx_d, dy_d = directions[move]
        next_X = x+dx_d
        next_Y = y+dy_d
        
        mazeObject.updateOrientation(move)
        
        if 0 <= next_Y < len(maze) and 0 <= next_X < len(maze[0]):
            if maze[next_Y][next_X] == 0:
                x = next_X
                y = next_Y
                mazeObject.updateX(x)
                mazeObject.updateY(y)
                mazeObject.clear()
                mazeObject.printMaze()
                time.sleep(0.3)
                
        
        if x==3 and y==0:
            break        

keepExecute = True
while keepExecute:
    action = input("This is the main script to compare results between Right Hand Rule and Genetic Algorithm (be sure to execute both to see results) \n \
Enter what you want to do : \n 1 : execute the maze resolution by right hand rule \n \
2 : execute the genetic algorithm \n q : stop execution \n")
    
    if action == "q":
        keepExecute = False
        break
        
    if action == "1":
        print("Executing right hand rule")
        print()
        rhSteps = executeRigthtHand()
        print()
            
    if action == "2":
        print("Executing Genetic Algorithm")
        print()
        gaResults, best_genome = executeGA()
        print(f"The best individual solved the maze the following way : {best_genome}")
        print()
        printGaMaze(genome=best_genome)       
        
        

# Now building the results
try:
    plt.figure(figsize=(12,5))
    
    plt.subplot(1,2,1)
    plt.plot(gaResults, label="Genetic algorithm", color="plum", linewidth=2)
    plt.title("Learning rate Genetic Algorithm")
    plt.xlabel("Generation")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True,alpha=0.3)
    
    plt.subplot(1,2,2)
    final_steps_ga = gaResults[-1]*100
    methods = ["Right Hand", "Genetic Algorithm"]
    steps = [rhSteps, final_steps_ga]
    plt.bar(methods, steps, color=["salmon","chartreuse"])
    plt.title("Final comparison between RHR and GA")
    plt.ylabel("Number of steps to find exit")
    
    for i,v in enumerate(steps):
        plt.text(i, v + 0.5, str(int(v)), ha='center', fontweight='bold')
    plt.tight_layout()
    plt.show(   )


except Exception as e:
    print(f"A problem occured, maybe you forgot to execute both GA and RHR. \n {e}")




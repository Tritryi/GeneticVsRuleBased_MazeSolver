from maze import Maze
import numpy as np
mazeObject = Maze()

"""
This file defines the genetic algorithm used to solve the maze.

- A gene is a number between 0 and 3 (refering to directions where North=0, East=1, South=2, West=3)
- A chromosom is a list of genes that are used to find a path to the exit. For example the chromosom [0, 1, 1, 2] means : 
    "go north, then go east, east again and finally go south"
    
We use a genome of 10 genes because the objective is to prove that it can do better than the right hand rule.

"""

population_size = 100
genome_length = 10
mutation_rate = 0.05

# Step 1 : populate
# creates 100 individuals : 100 tables which contains 30 values from 0 to 3
population = np.random.randint(0, 4, size=(population_size, genome_length))


# Step 2 : Fitness
# setting up our direction table
directions = [
    (0, -1), # 0 = North
    (1, 0),  # 1 = East
    (0, 1),  # 2 = South
    (-1, 0), # 3 = West
]

# useful variables
maze = mazeObject.getMaze()
start_x = mazeObject.getX()
start_y = mazeObject.getY() 

for gen in range(10):
    all_distances = []  

    # for each individual
    for p in population:
        # initialize x and y
        x = start_x
        y = start_y
        
        # for each gene (move)
        for move in p:
            # getting the moves based on directions
            dx_d, dy_d = directions[move]
            # computing the moves
            next_X = x + dx_d
            next_Y = y + dy_d
            
            # checking that we are not our of the maze
            if 0 <= next_Y < len(maze) and 0 <= next_X < len(maze[0]):
                # if the cell it targets is not a wall, we go on it. Otherwise, it does not move
                if maze[next_Y][next_X] == 0:
                    x = next_X
                    y = next_Y
            # if the end was reached, no need to keep going
            if x == 3 and y == 0:
                break
        # computes how close the individual is to the exit, we use absolute so that no difference is made between left/right or up/down
        dist = abs(x-3) + abs(y-0)
        all_distances.append(dist)
        
    # converts the distance array to a numpy array    
    distances_array = np.array(all_distances)
    # sort the results, closest individuals first, gives an indexes array 
    sorted_results = np.argsort(distances_array)

    print(f"--- Generation {gen} ---")
    print(f"Best individual : #{sorted_results[0]}, with {distances_array[sorted_results[0]]} steps away from the exit")
    print("-" *10)

    # Step 3 : Next Generation, the crossover
    best_individuals = sorted_results[:20]
    
    # preparing list for next generation 
    new_generation = []
    # saves the best inddividual
    new_generation.append(population[sorted_results[0]])
    
    # creating the new generation individuals
    # one is already kept as it is, we need 99 more
    for _ in range(population_size - 1):
        # taking two random parents among the 20 best
        index_parent1 = np.random.randint(0,20)
        index_parent2 = np.random.randint(0,20)
        
        parent1 = population[sorted_results[index_parent1]]
        parent2 = population[sorted_results[index_parent2]]
        
        # crossover 
        point = np.random.randint(1, genome_length)
        # creating a child
        child = np.concatenate([parent1[:point], parent2[point:]])
        
        # mutation        
        for i in range(genome_length):
            if np.random.rand() <= mutation_rate:
                child[i] = np.random.randint(0,4)
        
        new_generation.append(child)
        
    population = np.array(new_generation)
        
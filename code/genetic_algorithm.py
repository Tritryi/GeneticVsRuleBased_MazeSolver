from maze import Maze
import numpy as np
import matplotlib.pyplot as plt
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
best_score_per_gen = []

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
    # to store distances
    all_distances = []  

    # for each individual
    for p in population:
        # initialize x and y
        x = start_x
        y = start_y
        steps = 0 
        
        # for each gene (move)
        for move in p:
            # getting the moves based on directions
            dx_d, dy_d = directions[move]
            # computing the moves
            next_X = x + dx_d
            next_Y = y + dy_d
            
            # checking that we are not our of the maze
            if 0 <= next_Y < len(maze) and 0 <= next_X < len(maze[0]):
                # if the cell targeted is not a wall, it goes on it. Otherwise, it does not move
                steps +=1
                if maze[next_Y][next_X] == 0:
                    x = next_X
                    y = next_Y
            # if the end was reached, no need to keep going
            if x == 3 and y == 0:
                break
        # computes a score based on distance and steps done, the first part computes the distance to the exit, the second one is used to include steps in the result
        # with this if A : 0 + (9*0.1) and B : 0 + (6*0.1), B will get a better score because it requires less steps
        score = (abs(x-3) + abs(y-0)) + (steps*0.1)
        all_distances.append(score)
        
    # converts the distance array to a numpy array    
    distances_array = np.array(all_distances)
    # sort the results, best scored individuals first, gives an indexes array 
    sorted_results = np.argsort(distances_array)
    best_score_per_gen.append(distances_array[sorted_results[0]])

    print(f"--- Generation {gen} ---")
    print(f"Best individual : #{sorted_results[0]}, with {distances_array[sorted_results[0]]*10:.0f} steps away from the exit")
    print("-" *10)

    # Step 3 : Next Generation, the crossover    
    # preparing next generation and making sure best individual survives
    new_generation = []
    new_generation.append(population[sorted_results[0]])
    
    # creating the new generation individuals
    # one is already kept as it is, we need 99 more
    for _ in range(population_size - 1):
        # taking two random parents among the 20 best
        index_parent1 = np.random.randint(0,20)
        index_parent2 = np.random.randint(0,20)
        
        parent1 = population[sorted_results[index_parent1]]
        parent2 = population[sorted_results[index_parent2]]
        
        # crossover : take a random index
        point = np.random.randint(1, genome_length)
        # creating a child, parent1 gives 0 to point genes and parent2 gives point to genome_length genes
        child = np.concatenate([parent1[:point], parent2[point:]])
        
        # mutation        
        for i in range(genome_length):
            # takes a random number, if below mutation_rate a mutation occurs
            if np.random.rand() <= mutation_rate:
                child[i] = np.random.randint(0,4)
        
        new_generation.append(child)
    # the next population is set as the new one we created
    population = np.array(new_generation)


plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(best_score_per_gen, label="Genetic algorithm", color="blue", linewidth=2)
plt.title("Learning")
plt.xlabel("Generation")
plt.ylabel("Score (Distance + Steps)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
final_ia_steps = best_score_per_gen[-1]*10
methods = ["Right hand", "Genetic Algorithm"]
steps = [28, final_ia_steps]

plt.bar(methods, steps, color=["red","green"])
plt.title("Final comparison")
plt.ylabel("Number of steps to exit")

for i,v in enumerate(steps):
    plt.text(i, v + 0.5, str(int(v)), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()
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
def executeGA():
    population_size = 100 # for easy and medium maze
    # population_size = 600 # for complex maze
    genome_length = 10 # for easy and medium maze
    # genome_length = 80 # for complex maze
    mutation_rate = 0.05
    best_score_per_gen = []
    best_genome = None
    f = open("ga_results.txt", "w")
    f.write("--- GENETIC ALGORITHM RESULTS BY GENERATION---\n\n")

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
    
    for gen in range(10): # for easy and medium maze
    # for gen in range(15):  # for complex maze
        # to store distances
        all_scores = []  

        # for each individual
        for p in population:
            # initialize x and y
            x = start_x
            y = start_y
            steps = 0 
            
            # storing closest distance from the exit
            min_dist = abs(x-3) + abs(y-0)
            
            # for each gene (move)
            for move in p:
                # getting the moves based on directions
                dx_d, dy_d = directions[move]
                # computing the moves
                next_X = x + dx_d
                next_Y = y + dy_d
                
                # checking that we are not out of the maze
                if 0 <= next_Y < len(maze) and 0 <= next_X < len(maze[0]):
                    # if the cell targeted is not a wall, it goes on it. Otherwise, it does not move
                    if maze[next_Y][next_X] == 0:
                        x = next_X
                        y = next_Y
                        steps +=1
                        
                        # updating closest distance
                        current_dist = abs(x-3) + abs(y-0)
                        if current_dist < min_dist:
                            min_dist = current_dist

                # if the end was reached, no need to keep going
                if x == 3 and y == 0:
                    break
                
            if x == 3 and y == 0:
                # if the exit was found, we only use steps as a score
                score = steps *0.01
            else:
                # in case the exit was not found, the score is based on :
                # min_dist : the closest the individual was from the exit
                # +10 : ensures that an individual who didn't reach the exit has a bad score
                # (genome_length - steps)*0.01 : gives better score to an individual who made a lot of steps (exploring is nice)
                score = min_dist + 10 + (genome_length - steps) *0.01
            
            
            all_scores.append(score)
            
        # converts the distance array to a numpy array    
        scores_array = np.array(all_scores)
        # sort the results, best scored individuals first, gives an indexes array 
        sorted_results = np.argsort(scores_array)
        best_score_per_gen.append(scores_array[sorted_results[0]])
        best_genome = population[sorted_results[0]]

        f.write(f"--- Generation {gen} ---\n")
        f.write(f"Best individual : #{sorted_results[0]}, with a score of {scores_array[sorted_results[0]]:.2f}.\n")
        f.write("-" *10+"\n")

        # Step 3 : Next Generation, the crossover    
        # preparing next generation and making sure best individual survives
        new_generation = []
        new_generation.append(population[sorted_results[0]])
        
        # creating the new generation individuals
        # one is already kept as it is, we need 99 more
        for _ in range(population_size - 1):
            # taking two random parents among the 20 best
            index_parent1 = np.random.randint(0,20) # for easy and medium maze
            index_parent2 = np.random.randint(0,20) # for easy and medium maze
            # index_parent1 = np.random.randint(0,50) # for complex maze
            # index_parent2 = np.random.randint(0,50) # for complex maze
            
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
        
    


    f.close()
    return best_score_per_gen, best_genome
    
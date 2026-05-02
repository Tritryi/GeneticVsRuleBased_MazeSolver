from maze import Maze
import numpy as np
mazeObject = Maze()

"""
This file defines the genetic algorithm used to solve the maze.

- A gene is a number between 0 and 3 (refering to directions where North=0, East=1, South=2, West=3)
- A chromosom is a list of genes that are used to find a path to the exit. For example the chromosom [0, 1, 1, 2] means : 
    "go north, then go east, east again and finally go south"
    
Since the maze can be a bit big, we use a sequence of 30 genes that should be enough to exit.



"""

population_size = 100
genome_length = 30

# creates 100 individuals : 100 tables which contains 30 values from 0 to 3
population = np.random.randint(0, 4, size=(population_size, genome_length))

print(population[1])

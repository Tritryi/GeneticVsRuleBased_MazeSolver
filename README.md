# Genetic vs Right-hand rule Maze solving

This repository is used for my project of maze solving in Python. The idea here was inspired by *Physarum polycephalum* a type
of fungus that is well known to solve mazes better than any human algorithm. 
Knowing this, I decided to mimic this scenario in a Python project. The human algorithm  used here is the "right-hand rule" which states "keep your hand on the wall at your right to find the exit". The fungus will be mimicked by a genetic algorithm.


The goal is to determine which one gets better results which will be computed as "number of steps required to find the exit". Let me go through the different files that will be used here.

## Results and analyze
If you don't wish to execute the code and simply want to see the results, you can simply read my [Maze report](https://github.com/Tritryi/GeneticVsRuleBased_MazeSolver/blob/main/Maze_report.pdf).

## Files and their utility

### Maze.py
Defines the maze class, how the maze is constructed and useful methods. Three mazes are possible, uncomment the one you want to use.

### Colorization.py
Utility class that I created, used to make nice prints in the terminal easily

### Right_hand_rule.py
Defines the right-hand rule algorithm to solve the maze. It defines the pseudo algorithm and the actual one in the while loop. It also prints the number of steps made during the solve of the maze.

### Genetic_algorithm.py
Defines the genetic algorithm used to solve the maze. I initialized it with a population of 100 and 10 genes since, by looking at easy and medium mazes, we know it can be solved in 6 moves. The complex maze will require some changes in parameters.

# How to use ?

## Installation

To execute the algorithms and compare their results you will need to prepare a Python environment. Start by creating a virtual environment : 
```
git clone https://github.com/Tritryi/GeneticVsRuleBased_MazeSolver.git
cd GeneticVsRuleBased_MazeSolver/code/
python3 -m venv .venv
source .venv/bin/activate
```

Then install the required packages
```
pip install -r ../requirements.txt
```

## Execution
Simply execute the main script, the maze is set to the easy one by default but you can go to maze.py and uncomment the one you wish to use.
```
python3 main.py
```

The main script is interactive, make sure to execute every part in the order you wish.

## Note about complex maze
In order to find an optimal solution for the complex maze you need to actually change some parameters. Go to genetic_algorithm.py and change those parameters :
```
population_size = 600
genome_length = 80
parents = 50 best
generations = 15
```
You can simply uncomment some lines that will set the right parameters. The optimal solution for complex maze is 24 steps, you should see this between generation 10-13.

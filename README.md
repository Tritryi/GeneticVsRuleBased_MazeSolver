# Genetic vs Right-hand rule Maze solving

This repository is used for my project of maze solving in Python. The idea here was inspired by *Physarum polycephalum* a type
of fungus that is well known to solve mazes better than any human algorithm. 
Knowing this, I decided to mimic this scenario in a Python project. The human algorithm that is used here is the "right-hand rule" which states "keep your hand on the wall at your right to find the exit". The fungus will be mimicked by a genetic algorithm.

The goal is to determine which one gets better results which will be computed as "number of steps required to find the exit". Let me go through the different files that will be used here.

## Files and their utility

### Maze.py
Defines the maze class, how the maze is constructed and useful methods. Two mazes are possible, uncomment the one you want to use.

### Colorization.py
Utility class that I created, used to make nice prints in the terminal easily

### Right_hand_rule.py
Defines the right-hand rule algorithm to solve the maze. It defines the pseudo algorithm and the actual one in the while loop. It also prints the number of steps made during the solve of the maze.

## How to use ?

### Right-hand rule

To see the performance of the right-hand rule algorithm, start by uncommenting the maze you want to use as an example in `maze.py`. Then simply do this : 
```
python3 code/right_hand_rule.py
```
It should print you the maze solving step by step along with total number of steps made.

### Genetic algorithm
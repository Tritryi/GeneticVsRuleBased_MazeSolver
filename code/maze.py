from colorization import ColorTranslator
import os

class Maze():
    def __init__(self):
        self.maze = [
            [1,1,1,0,1],
            [1,0,0,0,1],
            [1,0,1,1,1],
            [0,0,0,0,1],
            [1,1,1,0,1],
            [1,1,1,1,1]
        ]
        # self.maze = [
        #     [1,1,1,0,1,1,1],
        #     [1,0,0,0,0,0,1],
        #     [1,0,1,1,1,1,1],
        #     [0,0,0,0,1,1,1],
        #     [1,1,1,0,0,0,1],
        #     [1,1,1,1,1,0,1],
        #     [1,1,1,0,0,0,1],
        #     [1,1,1,1,1,1,1]
        # ]
        # self.maze = [
        #     [1,1,1,0,1,1,1,1,1,1,1],
        #     [1,0,0,0,0,0,0,1,0,1,1],
        #     [1,1,1,1,1,0,1,0,0,1,1],
        #     [0,0,0,0,1,0,0,1,0,1,1],
        #     [1,1,1,0,0,1,0,1,0,1,1],
        #     [1,1,1,1,0,1,0,0,0,1,1],
        #     [1,1,1,1,0,1,1,1,0,1,1],
        #     [1,1,1,0,0,0,0,0,0,1,1],
        #     [1,1,1,1,1,1,1,1,1,1,1]
        # ]
        self.colorizer = ColorTranslator()
        self.px = 0
        self.py = 3
        self.orientation = 1
        self.arrows = ["\u2191", "\u2192", "\u2193", "\u2190"]
        
    def printMaze(self):
        for y,line in enumerate(self.maze):
            for x,cell in enumerate(line):
                if x == self.px and y == self.py:
                    arrow = self.arrows[self.orientation]
                    print(self.colorizer.colorfulPrint(f"{arrow}{arrow}", "red"), end="")
                elif cell == 1:
                    print(self.colorizer.colorfulPrint("\u2588\u2588", "white"), end="")
                else:
                    print(self.colorizer.colorfulPrint("  ", "white"), end="")
            print()
    
    def updateOrientation(self, orientation):
        self.orientation = orientation
    
    def getX(self):
        return self.px
    
    def getY(self):
        return self.py
    
    def getMaze(self):
        return self.maze
    
    def updateX(self, newX):
        self.px = newX
        
    def updateY(self, newY):
        self.py = newY    
        
    def clear(self):
        os.system('clear')





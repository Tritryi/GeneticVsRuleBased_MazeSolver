class ColorTranslator:
    def __init__(self):
        self.colors = {
            "black" : "\x1b[30m",
            "red" : "\x1b[31m",
            "green" : "\x1b[32m",
            "yellow": "\x1b[33m",
            "blue" : "\x1b[34m",
            "magenta" : "\x1b[35m",
            "cyan" : "\x1b[36m",
            "white" : "\x1b[37m"
        }
        self.reset = "\x1b[0m"
        
    
    def colorfulPrint(self,text: str, color: str) -> None:
        color_code = self.colors.get(color)
        if color_code == None:
            print(f"This color does not exist! See with \x1b[33mshowColors\x1b[0m")
            exit
        return color_code + text + self.reset
                  
        
    def showColors(self) -> None:
        print("Possible colors :")
        for nom in self.colors.keys():
            print(f"- {nom}")
import imageio
import sys
import os

class cMain:
    def __init__(self):
        self.xOutput = []
        
        self.xClearBit = "0"
        self.xSetBit = "1"
        self.xNewLine = "#"
        
        
    def Render(self, xInput):
        print("".join(xInput).replace("0", " ").replace("1", "█").replace("#", "\n"))
    
    
    
    def Main(self, xImage):
        
        for yI in range(len(xImage)):
            for xI in range(len(xImage[yI])):
                xColor = xImage[yI][xI]
                
                xR = 1 if xColor[0] < 255 / 2 else 0
                xG = 1 if xColor[1] < 255 / 2 else 0
                xB = 1 if xColor[2] < 255 / 2 else 0
        
                if xR + xG + xB > 1:
                    self.xOutput.append(self.xSetBit)
                
                else:
                    self.xOutput.append(self.xClearBit)
                    
            self.xOutput.append(self.xNewLine)
        
        self.Render(self.xOutput)
        return "".join(self.xOutput)
        
    
if __name__ == '__main__':
    cM = cMain()
    
    xPath = input("Datapath: ")
    xImage = imageio.imread(os.path.join(xPath, input("Filename: ")))
    
    print(cM.Main(xImage))
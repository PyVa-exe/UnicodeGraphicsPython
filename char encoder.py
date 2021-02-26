

class cMain:
    def __init__(self):
        self.xFontFile = open(".\char encoder data.txt", "r").read()
        
        self.xFontLineLen = 7
        
        self.xFontData = {}
        self.xOutput = [None for x in range(self.xFontLineLen)]
        self.xLineCounter = 0
        
        for xI in self.xFontFile.split("\n"):
            xLineData = xI.split(":")
            self.xFontData[xLineData[0]] = xLineData[1].replace('"', "")
                        
       
    def NewLine(self):
        for x in range(self.xFontLineLen):
            self.xOutput.append(None)
            
        self.xLineCounter += 1
    
    
    def CharEncode(self, xInput):
        
        for xInputIndex in xInput:
            
            if xInputIndex == "\n":
                self.NewLine()
                continue
            
            elif xInputIndex not in self.xFontData.keys():
                xIterFontData = self.xFontData["_"]
                        
            else:
                xIterFontData = self.xFontData[xInputIndex]
            
            for xI in range(self.xFontLineLen):
                if self.xOutput[xI + self.xLineCounter * self.xFontLineLen]:
                    self.xOutput[xI + self.xLineCounter * self.xFontLineLen] += xIterFontData.split("#")[xI]
                
                else:
                    self.xOutput[xI + self.xLineCounter * self.xFontLineLen] = xIterFontData.split("#")[xI]


        #remove nones
        
        xI = len(self.xOutput) - 1
        while xI != 0:
            if not self.xOutput[xI]:
                self.xOutput.pop(xI)
            
            xI -= 1
            
        print(self.xOutput)
            
        for xI in range(len(self.xOutput)):
            self.xOutput[xI] += "0"
        
        print("#".join(self.xOutput).replace("0", "█").replace("1", "░").replace("#", "\n"))

        print("#".join(self.xOutput))
    
    
if __name__ == '__main__':
    cM = cMain()


    xInput = None
    xAllInput = ""
    while True:
        xInput = input()
        if xInput == "":
            break
        
        
        xAllInput += xInput + "\n"

    cM.CharEncode(xAllInput.lower())
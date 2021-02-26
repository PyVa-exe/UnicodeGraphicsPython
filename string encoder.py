class cMain:
    def __init__(self):
        pass
    
    def cDecode(self, xInput):
        return xInput.replace("0", "█").replace("1", "░").replace("#", "\n")
    
    
if __name__ == '__main__':
    cM = cMain()
    
    xAll = ""
    xInput = None
    while True:
        xInput = input(": ")
        if xInput == "":
            break
        
        xAll += xInput + "\n"
    
    print(cM.cDecode(xAll))
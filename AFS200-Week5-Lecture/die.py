import random
class Die:

    SIDES = ['🎲','⚀','⚁','⚂','⚃','⚄','⚅']
 
    def __init__(self,sides=6):
        self.numOfSides = sides
        self.currentSideUp = 1

    def roll(self):
        self.currentSideUp = random.randint(1,self.numOfSides)
        return self.currentSideUp

    def getNumOfSide(self):
        return self.numOfSides

    def getCurrentSideUp(self):
        return self.currentSideUp
    
    def setNumOfSide(self,sides):
        self.numOfSides = sides
        
    def setCurrentSideUp(self,sideUp): 
        self.currentSideUp = sideUp
    
    def __str__(self) -> str:
        return f'{Die.SIDES[self.getCurrentSideUp()]} ({self.getCurrentSideUp()})'
    
    def __rep__(self) -> str:
        return f'{Die.SIDES[self.getCurrentSideUp()]} ({self.getCurrentSideUp()})'     
        
    def __eq__(self, __o: object) -> bool:
        return self.getCurrentSideUp() == __o.getCurrentSideUp()
    
    def __lt__(self, __o: object) -> bool:
        return self.getCurrentSideUp() < __o.getCurrentSideUp()
    
    def __gt__(self, __o: object) -> bool:
        return self.getCurrentSideUp() > __o.getCurrentSideUp() 
    
    def __add__(self, __o: object) -> int:
        return self.getCurrentSideUp() + __o.getCurrentSideUp() 
            
    def showDieFace(self):
	    print(f'{Die.SIDES[self.getCurrentSideUp()]} ({self.getCurrentSideUp()})',end=" ")
    

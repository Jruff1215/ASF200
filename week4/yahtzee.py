import random

class Die:
   def __init__(self, sides):
       self.sides = sides
       self.value = 0
   def roll(self):
       self.value = random.randrange(1, self.sides)
   
   def getCurrentFaceValue(self):
       return self.value
  
   def showDieFace(self):
       print(self.value)
Die1 = Die(2)
Die2 = Die(2)
Die3 = Die(2)
Die4 = Die(2)
Die5 = Die(2)
Die1.roll()
Die2.roll()
Die3.roll()
Die4.roll()
Die5.roll()
DieValue1 = Die1.getCurrentFaceValue()
DieValue2 = Die2.getCurrentFaceValue()
DieValue3 = Die3.getCurrentFaceValue()
DieValue4 = Die4.getCurrentFaceValue()
DieValue5 = Die5.getCurrentFaceValue()

print(f'({DieValue1}) ({DieValue2}) ({DieValue3}) ({DieValue4}) ({DieValue5}) ')
if DieValue1 == DieValue2 and DieValue2 == DieValue3 and DieValue3 == DieValue4 and DieValue4 == DieValue5:
    print("YAHTZEE!!!")
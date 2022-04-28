import die

class Magic8Ball(die.Die):
    ANSWERS = [ "It is certain",
                "It is decidedly so",
                "Without a doubt",
                "Yes definitely",
                "You may rely on it",
                "As I see it, yes",
                "Most likely",
                "Outlook good",
                "Yes",
                "Signs point to yes",
                "Reply hazy, try again",
                "Ask again later",
                "Better not tell you now",
                "Cannot predict now",
                "Concentrate and ask again",
                "Don't count on it",
                "My reply is no",
                "My sources say no",
                "Outlook not so good",
                "Very doubtful"]
    
    def __init__(self):
        die.Die.__init__(self,len(self.ANSWERS))
    
    def showMessage(self):
        print(f"{self.ANSWERS[self.getCurrentSideUp()-1]}")
        
    def shake(self):
        self.roll()
        

ball = Magic8Ball()

print(ball.ANSWERS)
print(Magic8Ball.ANSWERS)

print(ball.getNumOfSide())

print("Will It Rain Today?")
ball.shake()
print("Magic 8 Ball says -->",end=" ")
ball.showMessage()

print()

print("Will all of the Students in AFS-200 pass this course?")
ball.shake()
print("Magic 8 Ball says -->",end=" ")
ball.showMessage()

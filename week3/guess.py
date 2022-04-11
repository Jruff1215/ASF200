word_guess = "PURPLE"
guess_list = []
wordBoard = ["_", "_", "_", "_", "_", "_"]
def showBoard():
    print(" ".join(wordBoard))
#showBoard()
instances = []
def checkGuess(letterGuess):
    guess_list.append(letterGuess)
    found = word_guess.__contains__(letterGuess)
    #print(found)
    
    if found: 
       # instances = []
        
        for index in range(0, len(word_guess)):
            if (word_guess[index] == letterGuess):
                instances.append(index)
        #print(instances)
        for each in instances:
            #print(wordBoard[each])
            wordBoard[each] = letterGuess
        # print(wordBoard[each])
    return found

wrongGuesses = 5
winGame = False
print("Can you guess the secret color? ")
showBoard()

while wrongGuesses > 0 and winGame == False: 

    guess = input("Guess a letter: ").upper()
    alreadyGuessed = guess_list.__contains__(guess)
    print(alreadyGuessed)
    if alreadyGuessed:
        print("You've already guessed this letter")
    else: 
        if checkGuess(guess):
            print(instances)
            if len(instances) > 1:
                print("Yes there are " + str(len(instances)) + " " + guess)
            else:
                print("Yes there is a " + guess)
            instances = []
            showBoard()
            check = wordBoard.__contains__("_")
            if check == False:
                winGame = True
        else:
            wrongGuesses -=1
            print("I'm sorry but there is no letter " + guess + "in the word")
            print(f"You have {wrongGuesses} left. ")
            showBoard()
if wrongGuesses == 0:
    print("You lose!!! The secret word was " + word_guess) 
else:
    print("Congratulations!!! You Won!!")
import random

class TriviaQuestion():
    def __init__(self, questions, category, difficultyLevel, correctAnswer, incorrectAnswer, id):
        self.questions = questions
        self.category = category
        self.difficultyLevel = difficultyLevel
        self.correctAnswer = correctAnswer
        self.incorrectAnswer = incorrectAnswer
        self.id = id
        
    def getQuestions(self):
        return self.questions
    def getCategory(self):
        return self.category
    def getDifficultyLevel(self):
        return self.difficultyLevel
    def getCorrectAnswer(self):
        return self.correctAnswer
    def getIncorrectAnswer(self):
        return self.incorrectAnswer
    def getId(self):
        return self.id
    
    
    def getShuffledAnswers(self):
        answerList =  self.incorrectAnswer
        answerList.append(self.correctAnswer)
        random.shuffle(answerList)
        print(answerList)
        return answerList
class TriviaGame():
    def __init__(self):
       self.questions = [] 
       self.correct = []
       self.incorrect = []
    def addQuestion(self, question):
        self.questions.append(question)
    def getAllQuestions(self):
        return self.questions
    def refreshPage(self):
       self.questions = [] 
       self.correct = []
       self.incorrect = []

#id, numOfQuestions, difficultyLevel
    def getMultipleChoice(self, answers):
        
        for index in range(0, len(answers)):
            #print(answers[index])
            #print(self.questions[index].getCorrectAnswer())
            
            if answers[index] == self.questions[index].getCorrectAnswer():
                self.correct.append(self.questions[index])
            else:
                self.incorrect.append(self.questions[index])

import requests
from flask import Flask, render_template, request
from triviaquestion import TriviaGame, TriviaQuestion
app = Flask(__name__)

def getQuestions():
    URL = "https://opentdb.com/api.php?amount=10&category=15&type=multiple"
      
    try:
        response = requests.get(URL, timeout=5)
        
        response.raise_for_status()
            
        response_JSON = response.json()
            
        return response_JSON
        
    except requests.exceptions.HTTPError as errh:
        print(f"HTTPError - {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error - {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timout - {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception - {err}")

game = TriviaGame()

@app.route("/")
def getAllQuestions():
    #game = TriviaGame()
    game.refreshPage()
    questionData = getQuestions()
    num = 0
    for question in questionData["results"]:
        quest= question["question"]
        category = question["category"]
        difficulty = question['difficulty']
        correct_answer = question["correct_answer"]
        incorrect_answers = question["incorrect_answers"]
        id = num
        num = num + 1
        trivia = TriviaQuestion(quest, category, difficulty, correct_answer, incorrect_answers, id)
        game.addQuestion(trivia)
    questions = game.getAllQuestions()
    return render_template('questions.html', results = questions, )    


@app.route("/score", methods=["POST"])
def showAnswers():
    answers = []
    questions = game.getAllQuestions()
    #print(questions)
    for question in questions:
        
        answer = str(request.form.get(str(question.getId())))
        #print(answer)
        answers.append(answer)
    game.getMultipleChoice(answers)  
    print(game.correct, game.incorrect)
    return render_template('answers.html', content = game)    


if __name__ == "__main__":
    app.run()
    
#questions.html search will be similar have a way to get all my answers get value from all radio buttons and connect them to the id they belong to. 
#receive values for radio buttoons, finds if answer that shows is correct or not.
#return an array which answers were correct or not dependin on output. before in questions.html the for loop that iterates throught the questions and show on the page like the sample output.
#last question on 53.
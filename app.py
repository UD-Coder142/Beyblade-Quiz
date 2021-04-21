from flask import Flask, render_template, redirect, url_for

class Question:
    def __init__(self, name, options, correct_opt):
        self.name = name
        self.options =  options
        self.correct_opt = correct_opt

Question1 = Question(
    'Who is the current world champion in Beyblade Burst Surge?',
    ('Valt Aoi', 'Aiger Akabane', 'Delta Zakuro', 'Free De La Hoya'),
    'Valt Aoi'
)

Question2 = Question(
    'Who is the only blader of Turbo 4 whose Beyblade wasn\'t repaired after destruction?',
    ('Phi', 'Xavier Bogard', 'Hyde', 'Laban Vanot'),
    'Hyde'
)

Question3 = Question(
    'Who is the only member of Big 5 who wasn\'t there in the Semi-Finals of International Blader\'s Cup?',
    ('Shu Kurenai', 'Lui Shirosagi', 'Free De La Hoya', 'Silas Karlisle'),
    'Silas Karlisle'
)

Question4 = Question(
    'Which is the 6th season of Beyblade Burst?',
    ('Turbo', 'DB', 'Rise', 'Surge'),
    'DB'
)

Question5 = Question(
    'Who is Lain Valhala\'s partner in Legend Tag League Festival?',
    ('Valt Aoi', 'Shu Kurenai', 'Hyuga Hizashi', 'Ranjiro Kiyama'),
    'Shu Kurenai'
)

global Questions
Questions = [
    Question1,
    Question2,
    Question3,
    Question4,
    Question5
]

global answers
answers = []

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/start')
def start():
    stage = 0
    return redirect(url_for('game', stage=stage))

@app.route('/game/<int:stage>')
def game(stage):
    try:
        question = Questions[stage]
        return render_template('game.html', ask=question, no=stage+1)
    except:
        return redirect(url_for('results'))

@app.route('/change/<int:num>/<value>')
def change(num, value):
    param1 = num
    param2 = value

    answers.append(str(param2))
    return redirect(url_for('game', stage=param1))

@app.route('/results')
def results():
    question1 = answers[0]
    question2 = answers[1]
    question3 = answers[2]
    question4 = answers[3]
    question5 = answers[4]

    questions = [
        question1,
        question2,
        question3,
        question4,
        question5
    ]

    right_question1 = Questions[0].correct_opt
    right_question2 = Questions[1].correct_opt
    right_question3 = Questions[2].correct_opt
    right_question4 = Questions[3].correct_opt
    right_question5 = Questions[4].correct_opt

    rights = [
        right_question1,
        right_question2,
        right_question3,
        right_question4,
        right_question5
    ]

    right_questions = 0
    for i in range(5):
        if questions[i] == rights[i]:
            right_questions += 1
        else:
            continue

    return render_template('results.html', completed=right_questions)

@app.route('/')
def index():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=False)
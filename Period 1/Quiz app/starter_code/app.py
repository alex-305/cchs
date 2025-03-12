from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create_quiz():
    return render_template('create_quiz.html')

@app.route('/quiz/<quiz_id>')
def take_quiz(quiz_id):
    # The quiz_id is passed to the template so the client-side JS
    # can load the quiz from localStorage.
    return render_template('take_quiz.html', quiz_id=quiz_id)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'<h1>Hello, {name}!</h1>'
    return '''
        <form method="post">
            <label for="name">Enter your name:</label>
            <input type="text" name="name" required>
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
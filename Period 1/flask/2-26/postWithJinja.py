from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        content = request.form.get('content')
        return redirect(url_for('post', username=username, content=content))
    return render_template('form.html')

@app.route('/post')
def post():
    username = request.args.get('username', 'Anonymous')
    content = request.args.get('content', '')
    return render_template('post.html', username=username, content=content)

if __name__ == '__main__':
    app.run(debug=True)

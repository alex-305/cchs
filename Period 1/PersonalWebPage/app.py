from flask import Flask, render_template

app = Flask(__name__)

accomplishments_list = [
    {
        "title": "Example Title 1", 
        "description": "Example description 1"
    },
    {
        "title": "Example Title 2", 
        "description": "Example description 2"
        },
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/accomplishments")
def accomplishments():
    return render_template("accomplishments.html", accomplishments_list=accomplishments_list)

if __name__ == "__main__":
    app.run(debug=True)

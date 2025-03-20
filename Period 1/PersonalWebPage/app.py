from flask import redirect, render_template, request, url_for
from database import create_app, db, Comment

app = create_app()

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

comments = []

@app.route("/")
def home():
    comments = Comment.query.all()
    return render_template("index.html", comments=comments)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/accomplishments")
def accomplishments():
    return render_template("accomplishments.html", accomplishments_list=accomplishments_list)

@app.route("/add_comment", methods=["POST"])
def add_comment():
    content = request.form.get("content")

    if content:
        new_comment = Comment(content=content, username="Guest")
        db.session.add(new_comment)
        db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=2000)

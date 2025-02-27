from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

students = []

@app.route("/add/students", methods=["GET", "POST"])
def add_students():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            students.append(name)
        return redirect(url_for("view_students"))

    return render_template("add_students.html")

@app.route("/")
def view_students():
    return render_template("students.html", students=students)

@app.route("/remove_student", methods=["POST"])
def remove_student():
    name = request.form.get("name")
    if name in students:
        students.remove(name)
    return redirect(url_for("view_students"))

if __name__ == "__main__":
    app.run(debug=True)
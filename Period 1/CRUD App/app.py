from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

students = []  # List to store student names

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

@app.route("/student/remove/<int:index>", methods=["POST"])
def remove_student(index):
    if 0 <= index < len(students):  # Ensure valid index
        students.pop(index)
    return redirect(url_for("view_students"))

@app.route("/student/update/<int:index>", methods=["GET", "POST"])
def update_student(index):
    if request.method == "GET":
        if 0 <= index < len(students):  # Ensure index is valid
            return render_template("update_student.html", student=students[index], index=index)
        else:
            return redirect(url_for("view_students"))  # Redirect if index is invalid
    elif request.method == "POST":
        new_name = request.form.get("name")
        if 0 <= index < len(students) and new_name:  # Ensure valid index and input
            students[index] = new_name
        return redirect(url_for("view_students"))

if __name__ == "__main__":
    app.run(debug=True)
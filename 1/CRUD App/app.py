from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

students = ["Alice", "Bob", "Charlie"]

@app.route("/")
def view_students():
    return render_template("students.html", students=students)

@app.route('/student/create', methods=['POST'])
def create_student():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            students.append(name)
        return redirect(url_for('view_students'))

@app.route('/student/<int:index>/delete', methods=['POST'])
def delete_student(index):
    if request.method == 'POST':
        if index < len(students):
            students.pop(index)
        return redirect(url_for('view_students'))
    
@app.route('/student/<int:index>/update', methods=['GET','POST'])
def update_student(index):
    if request.method == 'GET':
        return render_template("update_student.html", index=index, student=students[index])
    elif request.method == 'POST':
        name = request.form.get('name')
        if name:
            students[index] = name
        return redirect(url_for('view_students'))

    


if __name__ == "__main__":
    app.run(debug=True)
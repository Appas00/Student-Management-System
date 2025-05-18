# app.py

from flask import Flask, render_template, request, redirect, url_for
from models import StudentManagement

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        st_id = request.form['st_id']
        st_name = request.form['st_name']
        st_marks = request.form['st_marks']
        success = StudentManagement.add_student(st_id, st_name, st_marks)
        if success:
            return redirect(url_for('view_students'))
        else:
            return "Student with this ID already exists!"
    return render_template('add_student.html')

@app.route('/students')
def view_students():
    students = StudentManagement.get_all_students()
    return render_template('view_students.html', students=students)

@app.route('/update/<st_id>', methods=['GET', 'POST'])
def update_student(st_id):
    student = StudentManagement.get_student_by_id(st_id)
    if not student:
        return "Student not found"
    if request.method == 'POST':
        new_name = request.form['st_name']
        new_marks = request.form['st_marks']
        StudentManagement.update_student(st_id, new_name, new_marks)
        return redirect(url_for('view_students'))
    return render_template('update_student.html', student=student)

@app.route('/delete/<st_id>')
def delete_student(st_id):
    StudentManagement.delete_student(st_id)
    return redirect(url_for('view_students'))

if __name__ == '__main__':
    app.run(debug=True)

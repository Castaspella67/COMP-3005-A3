from flask import Flask, render_template, request, redirect, url_for
from database_sessions import Session
from db_init import Student
from datetime import date
app = Flask(__name__)

@app.route("/")
def index():
    with Session() as session:
        students = session.query(Student).all()
        print("fetching all kids:")
        print(students)
        return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    with Session() as session:
        first_name=request.form["first_name"]
        last_name=request.form["last_name"]
        email=request.form["email"]
        enrollment_date=request.form["enrollment_date"]
        new_student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            enrollment_date=enrollment_date)
        session.add(new_student)
        session.commit()
        print(f"Added student: {first_name},{last_name} {email}.{enrollment_date}")
    return redirect(url_for("index"))

@app.route("/update/<int:student_id>", methods=["POST"])
def update_student(student_id):
    with Session() as session:
        student = session.get(Student, student_id)
        if student:
            student.email = request.form["email"]
            session.commit()
            print(f"Updating new email: {student.email} for student {student}")
    return redirect(url_for("index"))

@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    with Session() as session:
        student = session.get(Student, student_id)
        if student:
            session.delete(student)
            session.commit()
            print(f"removing child {student}")
    return redirect(url_for("index"))







if __name__ == "__main__":
    app.run(debug=True)

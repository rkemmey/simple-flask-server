from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg://rkemmey:hi@localhost/students"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

    def __repr__(self):
        return self.first_name

# returns all student objects 
@app.route('/students/', methods=['GET'])
def get_students():
    students = Students.query.all()
    formatted_students = []
    for stud in students:
        formatted_students.append(
            {
                "id": stud.id,
                "first_name": stud.first_name,
                "last_name": stud.last_name,
                "age": stud.age,
                "grade": stud.grade
            }
        )
    return jsonify(formatted_students)

# # returns students > 20 years old
# @app.route('/old_students/', methods=['GET'])
# def get_students():
#     return jsonify(students)

# # returns students < 21 years old
# @app.route('/young_students/', methods=['GET'])
# def get_students():
#     return jsonify(students)

# # returns students < 21 years old and grade = A
# @app.route('/advance_students/', methods=['GET'])
# def get_students():
#     return jsonify(students)

# # returns first_name, last_name
# @app.route('/student_names/', methods=['GET'])
# def get_students():
#     return jsonify(students)

# # returns student_name + age
# @app.route('/student_ages/', methods=['GET'])
# def get_students():
#     return jsonify(students)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, port=8000)

#app.run(debug=True, port=8000)
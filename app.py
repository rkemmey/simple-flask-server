from flask import Flask, jsonify

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

app = Flask('app')

# returns all student objects 
@app.route('/students/', methods=['GET'])
def get_students():
    return jsonify(students)

# returns students > 20 years old
@app.route('/old_students/', methods=['GET'])
def get_students():
    return jsonify(students)

# returns students < 21 years old
@app.route('/young_students/', methods=['GET'])
def get_students():
    return jsonify(students)

# returns students < 21 years old and grade = A
@app.route('/advance_students/', methods=['GET'])
def get_students():
    return jsonify(students)

# returns first_name, last_name
@app.route('/student_names/', methods=['GET'])
def get_students():
    return jsonify(students)

# returns student_name + age
@app.route('/student_ages/', methods=['GET'])
def get_students():
    return jsonify(students)

app.run(debug=True, port=8000)
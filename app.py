import sqlite3
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00143",
        "name": "Happe Malunes",
        "program": "BSIT",
        "year": 3,
        "section": "B"
    })


@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')
    return jsonify({
        "message": f"Hello, {name}!"
    })

@app.route('/grade')
def get_grade():
    try:
        score = float(request.args.get('score', 0))
    except ValueError:
        return jsonify({"error": "score must be a number"}), 400
    remark = "Very Good" if score >= 75 else "Needs Improvement"
    return jsonify({"score": score, "remark": remark})


@app.route('/students')
def get_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return jsonify([dict(student) for student in students])


@app.route('/students/<int:id>')
def get_student_by_id(id):
    conn = get_db_connection()
    student = conn.execute(
        'SELECT * FROM students WHERE id = ?', (id,)
    ).fetchone()
    conn.close()
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(dict(student))


# Additional task: students filtered by section, read from students.db
@app.route('/students/section/<section>')
def get_students_by_section(section):
    conn = get_db_connection()
    students = conn.execute(
        'SELECT * FROM students WHERE section = ? COLLATE NOCASE', (section,)
    ).fetchall()
    conn.close()
    return jsonify([dict(student) for student in students])


if __name__ == '__main__':
    app.run(debug=True)

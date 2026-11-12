import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    name TEXT NOT NULL,
    program TEXT NOT NULL,
    year INTEGER NOT NULL,
    section TEXT NOT NULL
)''')

cursor.execute("DELETE FROM students")
cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'students'")

students = [
    ('24-00143', 'Happe Malunes', 'BSIT', 3, 'B'),
    ('24-00144', 'Ana Garcia', 'BSIT', 3, 'A'),
    ('24-00145', 'Mark Lopez', 'BSCS', 3, 'A'),
    ('25-00201', 'Liza Ramos', 'BSIS', 2, 'B'),
    ('26-00310', 'Paolo Cruz', 'BSIT', 1, 'C')
]

cursor.executemany('''INSERT INTO students (student_id, name, program, year, section)
VALUES (?, ?, ?, ?, ?)''', students)

conn.commit()
conn.close()
print("Database created successfully.")

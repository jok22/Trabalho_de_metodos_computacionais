CREATE TABLE IF NOT EXISTS student(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    gender VARCHAR(1),
    age INTEGER,
    pw TEXT
);

CREATE TABLE IF NOT EXISTS teacher (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    gender VARCHAR(1),
    age INTEGER,
    pw TEXT
);

CREATE TABLE IF NOT EXISTS class(
    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_name VARCHAR(50),
    start_time TIME,
    end_time TIME
);

CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER,
    student_id INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES class (class_id),
    FOREIGN KEY (student_id) REFERENCES student (student_id),
    FOREIGN KEY (teacher_id) REFERENCES teacher (teacher_id)
);

"""
This module contains repositories for managing data related to a school database.
The repositories provide methods for inserting, deleting, and updating teacher, class,
and enrollment records in the database. Each repository is a subclass of the Database class,
which provides a context manager interface for managing the database connection.
Example usage:
    import database_handler
    teacher_repo = database_handler.TeacherRepository()
    teacher_repo.insert_teacher("Jonathas Santos")
"""


import sqlite3


class Database:
    """
    A context manager for managing connections to a SQLite database.
    Attributes:
    - path (str): The path to the SQLite database file.
    """
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.conn = sqlite3.connect(self.path)
        return self.conn.cursor()

    def __exit__(self, exc_class, exc, traceback):
        self.conn.commit()
        self.conn.close()


class StudentRepository(Database):
    """
    A repository for managing students in a database.
    """
    def insert_student(self, student_info: tuple) -> None:
        """
        Insert a new student record into the database.
        Args:
        - name (str): The name of the student to insert.
        Returns:
        - None
        """
        ignored_columns = ["student_id"]
        all_columns_query = "SELECT name FROM PRAGMA_TABLE_INFO('student');"
        with self as cursor:
            cursor.execute(all_columns_query)
            columns = [col[0] for col in cursor.fetchall()]

        for i in ignored_columns:
            columns.remove(i)

        string = f"INSERT INTO student ({', '.join(columns)})" \
                 f" VALUES ({', '.join(['?'] * len(columns))})"
        with self as cursor:
            cursor.execute(string, student_info)

    def delete_student(self, student_id: int) -> None:
        """
        Delete a student record from the database.
        Args:
        - student_id (int): The ID of the student to delete.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("DELETE FROM student WHERE student_id = ?", (student_id,))
            cursor.execute("DELETE FROM enrollments WHERE student_id = ?", (student_id,))

    def update_student(self, student_id, new_student_info: tuple):
        ignored_columns = ["student_id"]
        all_columns_query = "SELECT name FROM PRAGMA_TABLE_INFO('student');"
        with self as cursor:
            cursor.execute(all_columns_query)
            all_columns = [col[0] for col in cursor.fetchall()]

        set_query = []
        ign = 0
        for i in range(len(all_columns)):
            if all_columns[i] in ignored_columns:
                ign += 1
            elif new_student_info[i - ign]:
                set_query.append(f"{all_columns[i]} = ?")

        set_query = ', '.join(set_query)
        string = f"UPDATE student SET {set_query} WHERE student_id = ?"
        updated_student_info = [x for x in new_student_info if x]

        with self as cursor:
            cursor.execute(string, [*updated_student_info, student_id])

    def read_single_student(self, student_id: int) -> list:
        """
        Get a list of a single student and their ID from the database.

        Args:
        - student_id (int): The ID of the student to retrieve.

        Returns:
        - A list containing the student's ID, name, gender, and age.
        """
        with self as cursor:
            cursor.execute("SELECT student_id, name, gender, age FROM student WHERE student_id=?", (student_id,))
            return cursor.fetchone()
        
    def read_student(self) -> list:
        """
        Get a list of all students and their IDs from the database.

        Returns:
        - list: A list of (student_id, name, gender, age) tuples for all students in the database.
        """
        with self as cursor:
            cursor.execute("SELECT student_id, name, gender, age, pw FROM student")
            return cursor.fetchall()

    def read_columns(self) -> list:
        """
        Get a list of all students and their IDs from the database.
        Returns:
        - list: A list of (teacher_id, name) tuples for all teachers in the database.
        """
        with self as cursor:
            columns_name = cursor.execute("SELECT name FROM PRAGMA_TABLE_INFO('student');").fetchall()
            return columns_name 

class TeacherRepository(Database):
    """
    A repository for managing teachers in a database.
    """
    def insert_teacher(self, teacher_info: tuple) -> None:
        """
        Insert a new teacher record into the database.
        Args:
        - name (str): The name of the new teacher.
        Returns:
        - None
        """
        ignored_columns = ["teacher_id"]
        all_columns_query = "SELECT name FROM PRAGMA TABLE_INFO('teacher');"
        with self as cursor:
            cursor.execute(all_columns_query)
            all_columns = [col[0] for col in cursor.fetchall()]

        insert_columns = []
        for i in all_columns:
            ignore = False
            for j in ignored_columns:
                if i == j:
                    ignore = True
                    break
            if not ignore:
                insert_columns.append(i)

        string = f"INSERT INTO teacher ({', '.join(insert_columns)})" \
                 f" VALUES ({', '.join(['?'] * len(insert_columns))})"
        with self as cursor:
            cursor.execute(string, teacher_info)

    def delete_teacher(self, teacher_id: int) -> None:
        """
        Delete a teacher record from the database.
        Args:
        - teacher_id (int): The ID of the teacher to delete.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("DELETE FROM teacher WHERE teacher_id = ?", (teacher_id,))
            cursor.execute("DELETE FROM enrollments WHERE teacher_id =?", (teacher_id,))

    def update_teacher(self, teacher_id: int, new_teacher_info: tuple):
        ignored_columns = ["teacher_id"]
        all_columns_query = "SELECT name FROM PRAGMA_TABLE_INFO('teacher');"
        with self as cursor:
            cursor.execute(all_columns_query)
            all_columns = [col[0] for col in cursor.fetchall()]

        set_query = []
        ign = 0
        for i in range(len(all_columns)):
            if all_columns[i] in ignored_columns:
                ign += 1
            elif new_teacher_info[i - ign]:
                set_query.append(f"{all_columns[i]} = ?")

        set_query = ', '.join(set_query)
        string = f"UPDATE teacher SET {set_query} WHERE teacher_id = ?"
        updated_teacher_info = [x for x in new_teacher_info if x]

        with self as cursor:
            cursor.execute(string, [*updated_teacher_info, teacher_id])

    def read_single_teacher(self, teacher_id: int) -> list:
        """
        Get a list of a single teacher and their ID from the database.

        Args:
        - teacher_id (int): The ID of the teacher to retrieve.

        Returns:
        - A list containing the teacher's ID, name, gender, and age.
        """
        with self as cursor:
            cursor.execute("SELECT teacher_id, name, gender, age FROM teacher WHERE teacher_id=?", (teacher_id,))
            return cursor.fetchone()

    def read_teacher(self) -> list:
        """
        Get a list of all teachers and their IDs from the database.

        Returns:
        - list: A list of (teacher_id, name, gender, age) tuples for all teachers in the database.
        """
        with self as cursor:
            cursor.execute("SELECT teacher_id, name, gender, age, pw FROM teacher")
            return cursor.fetchall()

    def read_columns(self) -> list:
        """
        Get a list of all students and their IDs from the database.
        Returns:
        - list: A list of (teacher_id, name) tuples for all teachers in the database.
        """
        with self as cursor:
            columns_name = cursor.execute("SELECT name FROM PRAGMA_TABLE_INFO('teacher');").fetchall()
            return columns_name 

class ClassRepository(Database):
    """
    A repository for managing classes in a database.
    """
    def insert_class(self, name: str, start_time: str, end_time: str) -> None:
        """
        Insert a new class record into the database.
        Args:
        - name (str): The name of the new class.
        - start_time (str): The start time of the new class.
        - end_time (str): The end time of the new class.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("INSERT INTO class (class_name, start_time, end_time) VALUES (?, ?, ?)", (name, start_time, end_time))

    def delete_class(self, class_id: int) -> None:
        """
        Delete a class record from the database.
        Args:
        - class_id (int): The ID of the class to delete.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("DELETE FROM enrollments WHERE class_id = ?", (class_id,))
            cursor.execute("DELETE FROM class WHERE class_id = ?", (class_id,))

    def update_class(self, class_id: int, new_class_info: tuple):
        ignored_columns = ["class_id"]
        all_columns_query = "SELECT name FROM PRAGMA_TABLE_INFO('class');"
        with self as cursor:
            cursor.execute(all_columns_query)
            all_columns = [col[0] for col in cursor.fetchall()]

        set_query = []
        ign = 0
        for i in range(len(all_columns)):
            if all_columns[i] in ignored_columns:
                ign += 1
            elif new_class_info[i - ign]:
                set_query.append(f"{all_columns[i]} = ?")

        set_query = ', '.join(set_query)
        string = f"UPDATE class SET {set_query} WHERE class_id = ?"
        updated_class_info = [x for x in new_class_info if x]

        with self as cursor:
            cursor.execute(string, [*updated_class_info, class_id])

    def read_single_class(self, class_id: int) -> list:
        """
        Get a single class and its information from the database.
        Args:
        - class_id (int): The ID of the class to retrieve.
        Returns:
        - tuple: A tuple containing the class information (class_id, class_name, start_time, end_time).
        """
        with self as cursor:
            cursor.execute("SELECT class_id, class_name, start_time, end_time FROM class WHERE class_id=?", (class_id,))
            return cursor.fetchone()

    def read_class(self) -> list:
        """
        Get a list of all classes and their IDs from the database.
        Returns:
        - list: A list of (class_id, class_name, start_time, end_time) tuples for all classes in the database.
        """
        with self as cursor:
            cursor.execute("SELECT class_id, class_name, start_time, end_time FROM class")
            return cursor.fetchall()


class EnrollmentRepository(Database):
    """
    A repository for managing enrollments in a database.
    """

    def insert_enrollment(self, class_id: int, student_id: int, teacher_id: int) -> None:
        """
        Insert a new enrollment record into the database.
        Args:
        - class_id (int): The ID of the class the student is enrolled in.
        - student_id (int): The ID of the student being enrolled.
        - teacher_id (int): The ID of the teacher who is responsible for the class.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("INSERT INTO enrollments (class_id, student_id, teacher_id) VALUES (?, ?, ?)",
                           (class_id, student_id, teacher_id))

    def update_enrollment(self, enrollment_id: int, new_enrollment_info: tuple) -> None:
        """
        Update an existing enrollment record in the database.

        Args:
        - enrollment_id (int): The ID of the enrollment to update.
        - new_enrollment_info (tuple): A tuple containing the new information for the enrollment.
          The tuple must have the following format:
          (new_class_id: Optional[int], new_student_id: Optional[int], new_teacher_id: Optional[int])
          Use None to indicate that a column should not be updated.

        Returns:
        - None
        """
        ignored_columns = ["enrollment_id"]
        all_columns_query = "SELECT name FROM PRAGMA_TABLE_INFO('enrollments');"
        with self as cursor:
            cursor.execute(all_columns_query)
            all_columns = [col[0] for col in cursor.fetchall()]

        set_query = []
        ign = 0
        for i in range(len(all_columns)):
            if all_columns[i] in ignored_columns:
                ign += 1
            elif new_enrollment_info[i - ign] is not None:
                set_query.append(f"{all_columns[i]} = ?")

        set_query = ', '.join(set_query)
        string = f"UPDATE enrollments SET {set_query} WHERE enrollment_id = ?"
        updated_enrollment_info = [x for x in new_enrollment_info if x is not None]

        with self as cursor:
            cursor.execute(string, [*updated_enrollment_info, enrollment_id])

    def delete_enrollment(self, enrollment_id: int) -> None:
        """
        Delete an enrollment record from the database.
        Args:
        - enrollment_id (int): The ID of the enrollment to delete.
        Returns:
        - None
        """
        with self as cursor:
            cursor.execute("DELETE FROM enrollments WHERE enrollment_id =? ", (enrollment_id, ))

    def get_single_enrollments_info(self, enrollment_id: int) -> list:
        """Returns a list of dictionaries representing enrollment information with student, class, teacher, and class start and end times.
        Returns:
            list: A list of dictionaries, each representing an enrollment and containing the following keys:
                  - enrollment_id
                  - student_id
                  - student_name
                  - class_id
                  - class_name
                  - class_start_time
                  - class_end_time
                  - teacher_id
                  - teacher_name
        """
        with self as cursor:
            cursor.execute("""
                SELECT enrollments.enrollment_id, student.student_id, student.name, class.class_id, class.class_name, class.start_time, class.end_time, teacher.teacher_id, teacher.name
                FROM enrollments 
                JOIN student ON enrollments.student_id = student.student_id 
                JOIN class ON enrollments.class_id = class.class_id 
                JOIN teacher ON enrollments.teacher_id = teacher.teacher_id
                WHERE enrollments.enrollment_id = ?;
                """, (enrollment_id,))
            enrollments_info = cursor.fetchall()
            return enrollments_info

    def get_enrollments_info(self) -> list:
        """Returns a list of dictionaries representing enrollment information with student, class, teacher, and class start and end times.
        Returns:
            list: A list of dictionaries, each representing an enrollment and containing the following keys:
                  - enrollment_id
                  - student_id
                  - student_name
                  - class_id
                  - class_name
                  - class_start_time
                  - class_end_time
                  - teacher_id
                  - teacher_name
        """
        with self as cursor:
            cursor.execute("""
                SELECT enrollments.enrollment_id, student.student_id, student.name, class.class_id, class.class_name, class.start_time, class.end_time, teacher.teacher_id, teacher.name
                FROM enrollments 
                JOIN student ON enrollments.student_id = student.student_id 
                JOIN class ON enrollments.class_id = class.class_id 
                JOIN teacher ON enrollments.teacher_id = teacher.teacher_id;
            """)
            enrollments_info = cursor.fetchall()
            return enrollments_info

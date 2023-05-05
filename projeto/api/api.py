from flask import Flask, jsonify, request
import logging

class StudentEnrollmentAPI:
    def __init__(self, enrollments, passwords):
        self.enrollments = enrollments
        self.passwords = passwords
        self.app = Flask(__name__)
        print("hello")

        @self.app.route('/student/<int:student_id>')
        def get_student_enrollments(student_id):
            password = request.args.get('password')
            if student_id in self.passwords and password == self.passwords[student_id]:
                student_enrollments = []
                for enrollment in self.enrollments:
                    if enrollment[1] == student_id:
                        student_enrollments.append({
                            "course_name": enrollment[4],
                            "start_time": enrollment[5],
                            "end_time": enrollment[6],
                            "professor": enrollment[8]
                        })
                return jsonify(student_enrollments), 200, {'Content-Type': 'application/json; charset=utf-8'}
            else:
                return jsonify({"error": "Invalid student ID or password"}), 401, {'Content-Type': 'application/json; charset=utf-8'}

    def run(self):
        self.app.logger.setLevel(logging.ERROR)
        self.app.run(debug=False)


import json
import database.database_handler as db
import ui.interface as ui 
import api.api as api 

def menu():
    print("""
    *******************************
    *    ESCOLHA UMA APLICAÇÃO    *
    *******************************
    1. DIGITE 1 PARA SEGUIR AO SISTEMA DE GERENCIAMENTO ESCOLAR
    2. DIGITE 2 PARA ACIONAR A API:\n
    """)
    choice = int(input())
    return choice


def main():
    with open('config.json' , 'r') as f:
        config = json.load(f)
        path = config['path_to_db']

    student= db.StudentRepository(path)
    teacher= db.TeacherRepository(path)
    class_= db.ClassRepository(path)
    enrollment= db.EnrollmentRepository(path)

    
    c = menu()
    if c == 1:
        user_interface = ui.Interface(student, class_, teacher, enrollment)
        user_interface.login() 

    else:
        student  = student.read_student()
        enrollment = enrollment.get_enrollments_info()
        passwords = {student[0]: student[4] for student in student}

        a = api.StudentEnrollmentAPI(enrollment, passwords)
        a.run()
        
if __name__ == '__main__':
    main()

import random
import sys 

def quick_sort(array):
    if len(array) < 2:
        return array
      
    low, same, high = [], [], []
    pivot = array[random.randint(0, len(array) - 1)]
    
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quick_sort(low) + same + quick_sort(high)

class Interface:
  def __init__(self, student, class_, teacher, enrollment):
    self.student = student
    self.class_ = class_
    self.teacher = teacher
    self.enrollment = enrollment

  def main_menu(self):
    print("""
      *********************************
      *    STUDENT MANAGMENT SYSTEM   *
      *********************************
    """)

    print("""
    ***MENU***
    1. ALUNO
    2. PROFESSOR
    3. CLASSE
    4. MATRICULA
    5. SAIR 
    """)

    var = int(input("Digite uma opção: \n"))
    if var == 1:
      self.student_menu()
    if var == 2:
      self.teacher_menu()
    if var == 3:
      self.class_menu()
    if var == 4:
      self.enrollment_menu()
    if var == 5:
      sys.exit()

  def student_menu(self):
    while True:
      print("""
      ***MENU DO ESTUDANTE***
      1. ADICIONAR ALUNO
      2. PROCURAR ALUNO
      3. EXCLUIR ALUNO
      4. VER ALUNOS
      5. VOLTAR PARA O MENU PRINCIPAL
      6. SAIR 
      """)
      var = int(input("Digite uma opção: \n"))
      if var == 1:
        student_name = input("DIGITE O NOME DO ALUNO: \n")
        student_gender = input("DIGITE O GÊNERO DO ALUNO: \n")
        student_age = int(input("DIGITE A IDADE DO ALUNO: \n"))
        student_pw = input("DIGITE A SENHA DO ALUNO: \n")
        try: 
          self.student.insert_student(student_name, student_gender, student_age, student_pw)
        except Exception as e:
          print(f"ERROR: {str(e)}")
      if var == 2:
        opc = int(input("DIGITE O ID DO ALUNO QUE DESEJA PROCURAR: \n"))
        print(self.student.read_single_student(opc))
      if var == 3:
        opc = int(input("DIGITE O ID DO ALUNO QUE DESEJA EXCLUIR: \n"))
        try: 
          self.student.delete_student(opc)
          print("DELETADO COM SUCESSO") 
        except Exception as e:
          print(f"ERROR: {str(e)}")
          bool_ = 0
      if var == 4:
        print("""
        *** SORTING MENU ***
        DESEJA VER APENAS OS NOMES DOS ALUNOS EM ORDEM ALFABETICA?
        DIGITE 1 PARA "SIM"
        DIGITE 0 PARA "NAO" 
        """) 
        opc = int(input())
        if opc == 1:
            students = self.student.read_student()
            print(students)
            student_names = [students[1] for students in students[1]]
            sorted_students = quick_sort(student_names)
        else:    
            foo = self.student.read_student()
            for tupla in foo:
                print(tupla)
      if var == 5:
        self.main_menu() 
      if var == 6:
        sys.exit()
        
  def teacher_menu(self):
    while True:
      print("""
      ***MENU DO PROFESSOR***
      1. ADICIONAR PROFESSOR
      2. PROCURAR PROFESSOR
      3. EXCLUIR PROFESSOR
      4. VER PROFESSORES 
      5. VOLTAR PARA O MENU PRINCIPAL
      6. SAIR 
      """)
      var = int(input("DIGITE UMA OPÇÃO: \n"))
      if var == 1:
        teacher_name = input("DIGITE O NOME DO PROFESSOR: \n")
        teacher_gender= input("DIGITE O GÊNERO DO PROFESSOR: \n")
        teacher_age = int(input("DIGITE A IDADE DO PROFESSOR: \n"))
        teacher_pw = input("DIGITE A SENHA DO PROFESSOR: \n")
        try: 
          self.teacher.insert_teacher(teacher_name, teacher_gender, teacher_age, teacher_pw)
        except Exception as e:
          print(f"ERROR: {str(e)}")
          bool_ = 0
      if var == 2:
        opc = int(input("DIGITE O ID DO PROFESSOR QUE DESEJA PROCURAR: \n"))
        print(self.student.read_single_student(opc))
      if var == 3:
        opc = int(input("DIGITE O ID DO PROFESSOR QUE DESEJA EXCLUIR: \n"))
        try: 
          self.teacher.delete_teacher(opc)
          print("DELETADO COM SUCESSO") 
        except Exception as e:
          print(f"ERROR: {str(e)}")
      if var == 4:
        print("""
        *** SORTING MENU ***
        DESEJA VER APENAS OS NOMES DOS PROFESSORES EM ORDEM ALFABETICA?
        DIGITE 1 PARA "SIM"
        DIGITE 0 PARA "NAO" 
        """) 
        opc = int(input())
        if opc == 1:
            teachers = self.teacher.read_teacher()
            teacher_names = [teachers[1] for teachers in teachers]
            sorted_teachers = quick_sort(teacher_names)
            print(sorted_teachers)
        else:    
            foo = self.teacher.read_teacher()
            for tupla in foo:
                print(tupla)
      if var == 5:
        self.main_menu() 
      if var == 6:
        sys.exit()
        
  def class_menu(self):
    while True:      
      print("""
      ***MENU DA DISCIPLINA***
      1. ADICIONAR DISCIPLINA
      2. PROCURAR TURMA
      3. EXCLUIR TURMA
      4. VER TURMAS
      5. VOLTAR PARA O MENU PRINCIPAL
      6. SAIR 
      """)
      var = int(input("DIGITE UMA OPÇÃO: \n")) 
      if var == 1:
        class_name = input("DIGITE O NOME DA DISCIPLINA: \n")
        class_start_time = input("DIGITE O HORÁRIO DO INÍCIO DA AULA. EX: 08:00:00: \n")
        class_end_time = input("DIGITE O HORÁRIO DO FIM DA AULA. EX: 10:00:00: \n")
        try:
          self.class_.insert_class(class_name, class_start_time, class_end_time)
        except Exception as e:
          print(f"ERROR: {str(e)}")
          bool_ = 0 
      if var == 2:
        opc = int(input("DIGITE O ID DA TURMA QUE DESEJA PROCURAR: \n "))
        print(self.class_.read_single_class(opc))
      if var == 3:
        opc = int(input("DIGITE O ID DA TURMA QUE DESEJA EXCLUIR: \n "))
        try:
          self.class_delete_class(opc)
        except Exception as e:
          print(f"ERROR: {str(e)}")          
      if var == 4:
        foo = self.class_.read_class()
        for tupla in foo:
            print(tupla)
      if var == 5:
        self.main_menu()
      if var == 6:
        sys.exit() 

  def enrollment_menu(self):
    while True:      
      print("""
      ***MENU DE MATRICULA***
      1. ADICIONAR MATRICULA
      2. PROCURAR MATRICULA
      3. EXCLUIR MATRICULA
      4. VER MATRICULAS
      5. VOLTAR PARA O MENU PRINCIPAL
      6. SAIR 
      """)
      var = int(input("DIGITE UMA OPÇÃO: \n")) 
      if var == 1:
        class_id = int(input("DIGITE O ID DA TURMA: \n"))
        student_id = int(input("DIGITE O ID DO ALUNO: \n")) 
        teacher_id = int(input("DIGITE O ID DO PROFESSOR: \n"))
        try:
          self.enrollment.insert_enrollment(class_id, student_id, teacher_id)
        except Exception as e:
          print(f"ERROR: {str(e)}")
      if var == 2:
        opc = int(input("DIGITE O ID DA MATRICULA QUE DESEJA PROCURAR: \n"))
        print(self.enrollment.get_single_enrollments_info(opc))
      if var == 3:
        opc = int(input("DIGITE O ID DA MATRICULA QUE DESEJA EXCLUIR: \n"))
        try: 
          self.enrollment.delete_enrollment(opc)
          print("DELETADO COM SUCESSO") 
        except Exception as e:
          print(f"ERROR: {str(e)}")
      if var == 4:
        print(self.enrollment.get_enrollments_info())
      if var == 5:
        self.main_menu() 
      if var == 6:
        sys.exit()

    def return_enrollments(self):
        return self.enrollment.get-enrollments_info() 

        

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
  def login(self):
    usuarios_senhas = {"admin": "1234"}
    while True:
      print("""
      *********************************
      *             LOGIN             *
      *********************************
    """)
      usuario = input("Digite seu nome de usuário: ")
      senha = input("Digite sua senha: ")
      if usuario in usuarios_senhas and senha == usuarios_senhas[usuario]:
        print("Login realizado com sucesso!")
        self.main_menu()
      else:
        print("Nome de usuário ou senha incorretos.")
  def feedback(self):
    print("""
    
    ***OBRIGADO PELA PREFERÊNCIA***
      
    VOCÊ PODE DAR UM FEEDBACK PARA OS DEVS?
    1.Sim.
    2.Não, deixa para a próxima.\n
    """)
    fim = int(input("Digite uma opção: "))
    if fim==1: 
      fd=input("Escreva aqui seu Feedback:")
      print("Obrigado pelo feedback, até a próxima!!")
      sys.exit()
    if fim==2:
      print("Obrigado, até a próxima!!")
      sys.exit()
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
      self.feedback()

  def student_menu(self):
    while True:
      print("""
      ***MENU DO ESTUDANTE***
      1. ADICIONAR ALUNO
      2. PROCURAR ALUNO
      3. EXCLUIR ALUNO
      4. VER ALUNOS
      5. EDITAR ALUNO
      6. VOLTAR PARA O MENU PRINCIPAL
      7. SAIR 
      """)
      var = int(input("Digite uma opção: \n"))
      if var == 1:
        student_name = input("DIGITE O NOME DO ALUNO: \n")
        student_gender = input("DIGITE O GÊNERO DO ALUNO: \n")
        student_age = int(input("DIGITE A IDADE DO ALUNO: \n"))
        student_pw = input("DIGITE A SENHA DO ALUNO: \n")
        try: 
          self.student.insert_student(student_name, student_gender, student_age, student_pw)
          print("ALUNO ADCIONADO COM SUCESSO!")
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
            student_names = [students[1] for students in students]
            sorted_students = quick_sort(student_names)
            print(sorted_students)
            
        else:    
            foo = self.student.read_student()
            print(self.student.read_columns())
            for tupla in foo:
                print(tupla)
      if var == 5:
        student_id = input("DIGITE O ID DO ALUNO: \n")
        student_name = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE O NOVO NOME DO ALUNO: \n")
        student_name = None if not student_name else student_name
        student_gender = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE O NOVO GÊNERO DO ALUNO: \n")
        student_gender = None if not student_gender else student_gender
        student_age = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE A NOVA IDADE DO ALUNO: \n")
        student_age = int(student_age) if student_age else None
        student_pw = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE A NOVA SENHA DO ALUNO: \n")
        student_pw = None if not student_pw else student_pw
        try:
          self.student.update_student(student_id, (student_name, student_gender, student_age, student_pw))
          print("ALUNO ATUALIZADO COM SUCESSO!")
        except Exception as e:
          print(f"ERROR: {str(e)}")
      if var == 6:
        self.main_menu()
      if var == 7:
        sys.exit()
        
  def teacher_menu(self):
    while True:
      print("""
      ***MENU DO PROFESSOR***
      1. ADICIONAR PROFESSOR
      2. PROCURAR PROFESSOR
      3. EXCLUIR PROFESSOR
      4. VER PROFESSORES 
      5. EDITAR PROFESSOR
      6. VOLTAR PARA O MENU PRINCIPAL
      7. SAIR 
      """)
      var = int(input("DIGITE UMA OPÇÃO: \n"))
      if var == 1:
        teacher_name = input("DIGITE O NOME DO PROFESSOR: \n")
        teacher_gender= input("DIGITE O GÊNERO DO PROFESSOR: \n")
        teacher_age = int(input("DIGITE A IDADE DO PROFESSOR: \n"))
        teacher_pw = input("DIGITE A SENHA DO PROFESSOR: \n")
        try: 
          self.teacher.insert_teacher(teacher_name, teacher_gender, teacher_age, teacher_pw)
          print("PROFESSOR ADCIONADO COM SUCESSO!")
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
            print(self.teacher.read_columns())
            for tupla in foo:
                print(tupla)
      if var == 5:
        teacher_id = input("DIGITE O ID DO PROFESSOR: \n")
        teacher_name = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE O NOVO NOME DO PROFESSOR: \n")
        teacher_name = None if not teacher_name else teacher_name
        teacher_gender = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE O NOVO GÊNERO DO PROFESSOR: \n")
        teacher_gender = None if not teacher_gender else teacher_gender
        teacher_age = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE A NOVA IDADE DO PROFESSOR: \n")
        teacher_age = int(teacher_age) if teacher_age else None
        teacher_pw = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE A NOVA SENHA DO PROFESSOR: \n")
        teacher_pw = None if not teacher_pw else teacher_pw
        try:
          self.teacher.update_teacher(teacher_id, (teacher_name, teacher_gender, teacher_age, teacher_pw))
          print("PROFESSOR ATUALIZADO COM SUCESSO!")
        except Exception as e:
          print(f"ERROR: {str(e)}")
      if var == 6:
        self.main_menu()
      if var == 7:
        self.feedback()
        
  def class_menu(self):
    while True:      
      print("""
      ***MENU DA DISCIPLINA***
      1. ADICIONAR DISCIPLINA
      2. PROCURAR TURMA
      3. EXCLUIR TURMA
      4. VER TURMAS
      5. EDITAR TURMA
      6. VOLTAR PARA O MENU PRINCIPAL
      7. SAIR 
      """)
      var = int(input("DIGITE UMA OPÇÃO: \n")) 
      if var == 1:
        class_name = input("DIGITE O NOME DA DISCIPLINA: \n")
        class_start_time = input("DIGITE O HORÁRIO DO INÍCIO DA AULA. EX: 08:00:00: \n")
        class_end_time = input("DIGITE O HORÁRIO DO FIM DA AULA. EX: 10:00:00: \n")
        print("TURMA ADCIONADA COM SUCESSO!")
        try:
          self.class_.insert_class(class_name, class_start_time, class_end_time)
          print("DISCIPLINA ADCIONADA COM SUCESSO!")
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
        class_id = input("DIGITE O ID DA TURMA: \n")
        class_name = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE O NOVO NOME DA TURMA: \n")
        class_name = None if not class_name else class_name
        start_time = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE O NOVO HORÁRIO DO INÍCIO DA AULA: \n")
        start_time = None if not start_time else start_time
        end_time = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE O NOVO HORÁRIO DO FIM DA AULA: \n")
        end_time = None if not end_time else end_time
        try:
          self.class_.update_class(class_id, (class_name, start_time, end_time))
          print("DISCIPLINA ATUALIZADA COM SUCESSO!")
        except Exception as e:
          print(f"ERROR: {str(e)}")
      if var == 6:
        self.main_menu()
      if var == 7:
        self.feedback()

  def enrollment_menu(self):
    while True:      
      print("""
      ***MENU DE MATRICULA***
      1. ADICIONAR MATRICULA
      2. PROCURAR MATRICULA
      3. EXCLUIR MATRICULA
      4. VER MATRICULAS
      5. EDITAR MATRICULAS
      6. VOLTAR PARA O MENU PRINCIPAL
      7. SAIR 
      """)
      var = int(input("DIGITE UMA OPÇÃO: \n")) 
      if var == 1:
        class_id = int(input("DIGITE O ID DA TURMA: \n"))
        student_id = int(input("DIGITE O ID DO ALUNO: \n")) 
        teacher_id = int(input("DIGITE O ID DO PROFESSOR: \n"))
        try:
          self.enrollment.insert_enrollment(class_id, student_id, teacher_id)
          print("MATRICULA ADCIONADA COM SUCESSO!")
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
        enrollment_id = input("DIGITE O ID DA MATRICULA: \n")
        class_id = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE O NOVO ID DA TURMA: \n")
        class_id = int(class_id) if class_id else None
        student_id = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE O NOVO ID DO ALUNO: \n")
        student_id = int(student_id) if student_id else None
        teacher_id = input("CASO NÃO QUEIRA MUDAR, APENAS CONFIRME\nDIGITE O NOVO ID DO PROFESSOR: \n")
        teacher_id = int(teacher_id) if teacher_id else None
        try:
          self.enrollment.update_enrollment(enrollment_id, (class_id, student_id, teacher_id))
          print("MATRICULA ATUALIZADA COM SUCESSO!")
        except Exception as e:
          print(f"ERROR: {str(e)}")
      if var == 6:
        self.main_menu()
      if var == 7:
        self.feedback()

    def return_enrollments(self):
        return self.enrollment.get-enrollments_info() 

        

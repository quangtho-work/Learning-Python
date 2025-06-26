
from dto import studentDto, subjectDto, gradeDto
from models import student, subject, grade
ListStudent: list[student.Student] = []
ListGrade: list[grade.Grade]=[]
ListSubject: list[subject.Subject]= []
def display_menu():
    while True:
        print("=== Student and Subject Management ===")
        print("1. Student")
        print("2. Grade")
        print("3. Subject")
        print("4. Exit")
        print("======================================")
        choice = get_user_choice()
        if choice == '1':
            display_student_menu()
        elif choice == '2':
            display_grade_menu()
        elif choice == '3':
            display_subject_menu()
        elif choice == '4':
            print("Exiting the application.")
            break

def get_user_choice():
    choice = input("Enter your choice: ")
    return choice
def display_student_menu():
    while True:
        print("=== Student Menu ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back to Main Menu")
        print("======================================")
        choice = get_user_choice()
        if choice == '1':
            Add_student()
        elif choice == '2':
            View_students()
        elif choice == '3':
            Update_student()
        elif choice == '4':
            Delete_student()
        elif choice == '5':
            print("Exiting the application.")
            break
def Add_student():
    print("input student name, age and gender")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    gender = input("Enter student gender: ")
    stu = student.Student(name, age, gender)
    if studentDto.addStudent(stu):
        print("Student added successfully.")
    else :
        print("Failed to add student and grade.")
def View_students():
    ListStudent = studentDto.getStudentList()
    if ListStudent:
        for student in ListStudent:
            print(student)
            print("----------------------------------------")
    else:
        print("List is empty")
def Update_student():
    id = input("input id student: ")
    stu: student.Student = studentDto.getStudentById(id)
    if stu:
        print(stu)
        name = input("re-enter student name: ")
        age = input("re-enter student age: ")
        gender = input("re-enter student gender: ")
        stu.name =name
        stu.age = age
        stu.gender = gender
        if studentDto.updateStudent(stu):
            print("Student update successfully.")
        else :
            print("Failed to update student .")
    else:
        print("Not Found")
def Delete_student():
    id = input("input id student: ")
    stu: student.Student = studentDto.getStudentById(id)
    if stu:
        print(stu)
        if studentDto.deleteStudent(id):
            print("Student delete successfully.")
        else :
            print("Failed to delete student .")
    else:
        print("Not Found")

      
def display_grade_menu():
    while True:
        print("=== Grade Menu ===")
        print("1. Add Grade")
        print("2. View Grades")
        print("3. Update Grade")
        print("4. Delete Grade")
        print("5. Back to Main Menu")
        print("======================================")
        choice = get_user_choice()
        if choice == '1':
            Add_grade()
        elif choice == '2':
            View_grades()
        elif choice == '3':
            Update_grade()
        elif choice == '4':
            Delete_grade()
        elif choice == '5':
            break

def Add_grade():
    ListSubject = subjectDto.getSubjectList()
    if ListSubject:
        id = input("input id student: ")
        stu: student.Student = studentDto.getStudentById(id)
        if stu:
            print(stu)
            tempGradeList = []  # Sử dụng list tạm thời
            for subject_item in ListSubject:
                print(f"Subject Name: {subject_item.name}")
                score = input("Enter score: ")
                g = grade.Grade(id, subject_item.subject_id, score)
                tempGradeList.append(g)
            if gradeDto.addGrade(tempGradeList):
                print("Grade added successfully.")
            else:
                print("Failed to add grade.")
        else:
            print("Not Found")
    else:
        print("Subject is empty")

def View_grades():
    student_id = input("Enter student id to view grades (leave blank to view all): ")
    if student_id.strip() == "":
        ListGrade = gradeDto.getGradesOfAllStudents()
    else:
        ListGrade = gradeDto.getGrades(student_id)
    if ListGrade:
        for g in ListGrade:
            stu: student.Student = studentDto.getStudentById(g.student_id)
            print(stu)
            sub: subject.Subject = subjectDto.getSubjectById(g.subject_id)
            print(sub)
            print(g)
            print("----------------------------------------")
    else:
        print("No grades found.")

def Update_grade():
    student_id = input("Enter student id: ")
    subject_id = input("Enter subject id: ")
    score = input("Enter new score: ")
    g = grade.Grade(student_id, subject_id, score)
    if gradeDto.updateGrade([g]):
        print("Grade updated successfully.")
    else:
        print("Failed to update grade.")

def Delete_grade():
    student_id = input("Enter student id: ")
    subject_id = input("Enter subject id: ")
    if gradeDto.deleteGrade(student_id, subject_id):
        print("Grade deleted successfully.")
    else:
        print("Failed to delete grade.")

def display_subject_menu():
    while True:
        print("=== Subject Menu ===")
        print("1. Add Subject")
        print("2. View Subjects")
        print("3. Update Subject")
        print("4. Delete Subject")
        print("5. Back to Main Menu")
        print("======================================")
        choice = get_user_choice()
        if choice == '1':
            Add_subject()
        elif choice == '2':
            View_subjects()
        elif choice == '3':
            Update_subject()
        elif choice == '4':
            Delete_subject()
        elif choice == '5':
            break

def Add_subject():
    name = input("Enter subject name: ")
    sub = subject.Subject(name)
    if subjectDto.addSubject(sub):
        print("Subject added successfully.")
    else:
        print("Failed to add subject.")

def View_subjects():
    subjects = subjectDto.getSubjectList()
    if subjects:
        for sub in subjects:
            print(sub)
            print("----------------------------------------")
    else:
        print("No subjects found.")

def Update_subject():
    subject_id = input("Enter subject id: ")
    sub = subjectDto.getSubjectList()
    found = False
    if sub:
        for s in sub:
            if str(s[0]) == subject_id:
                found = True
                print(s)
                name = input("Re-enter subject name: ")
                subject_obj = subject.Subject(name, subject_id=s[0])
                if subjectDto.updateSubject(subject_obj):
                    print("Subject updated successfully.")
                else:
                    print("Failed to update subject.")
                break
    if not found:
        print("Not Found")

def Delete_subject():
    subject_id = input("Enter subject id: ")
    if subjectDto.deleteSubject(subject_id):
        print("Subject deleted successfully.")
    else:
        print("Failed to delete subject.")

if __name__ == "__main__":
    display_menu()
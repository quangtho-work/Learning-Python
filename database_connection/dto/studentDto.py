import dbConnection
from models import student, grade

def getStudentList():  # lấy danh sách sinh viên
    conn = None
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "SELECT student_id, name, age, gender FROM students"
        cursor.execute(sql)
        rows = cursor.fetchall()
        students = []
        for row in rows:
            stu = student.Student(row[1], row[2], row[3], student_id=row[0])
            students.append(stu)
        cursor.close()
        return students
    except Exception as e:
        print("Error connecting to the database:", e)
    finally:
        if conn:
            conn.close()
    return None

def getStudentById(id):  # lấy sinh viên theo id
    conn = None
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "SELECT student_id, name, age, gender FROM students WHERE student_id = %s"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return student.Student(row[1], row[2], row[3], student_id=row[0])
        return None
    except Exception as e:
        print("Error connecting to the database:", e)
    finally:
        if conn:
            conn.close()
    return None

def addStudent(stu: student.Student):  # thêm sinh viên
    conn = None
    try:
        conn = dbConnection.getConnection()
        if conn is None:
            return False
        cursor = conn.cursor()
        sql = "INSERT INTO students (name, age, gender) VALUES (%s, %s, %s)"
        cursor.execute(sql, (stu.name, stu.age, stu.gender))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error connecting to the database:", e)
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    return False

def updateStudent(stu: student.Student):  # sửa sinh viên
    conn = None
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "UPDATE students SET name=%s, age=%s, gender=%s WHERE student_id=%s"
        cursor.execute(sql, (stu.name, stu.age, stu.gender, stu.student_id))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error connecting to the database:", e)
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    return False

def deleteStudent(id):  # xóa sinh viên
    conn = None
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "DELETE FROM students WHERE student_id=%s"
        cursor.execute(sql, (id,))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error connecting to the database:", e)
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()
    return False
import dbConnection
from models import grade

def getGrades(student_id):  # lấy danh sách điểm của 1 sinh viên
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "SELECT student_id, subject_id, score FROM grades WHERE student_id = %s"
        cursor.execute(sql, (student_id,))
        grades = []
        for row in cursor.fetchall():
            grades.append(grade.Grade(row[0], row[1], row[2]))
        cursor.close()
        conn.close()
        return grades
    except Exception as ex:
        print(ex)
        return None

def getGradesOfAllStudents():
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "SELECT student_id, subject_id, score FROM grades ORDER BY student_id"
        cursor.execute(sql)
        grades = []
        for row in cursor.fetchall():
            grades.append(grade.Grade(row[0], row[1], row[2]))
        cursor.close()
        conn.close()
        return grades
    except Exception as ex:
        print(ex)
        return None

def addGrade(listGrade: list[grade.Grade]):  # thêm list điểm vào bảng grade
    conn = None
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "INSERT INTO grades (student_id, subject_id, score) VALUES (%s, %s, %s)"
        for g in listGrade:
            cursor.execute(sql, (g.student_id, g.subject_id, g.score))
        conn.commit()
        cursor.close()
        return True
    except Exception as ex:
        print(ex)
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()

def updateGrade(listGrade: list[grade.Grade]):  # cập nhật điểm của 1 sinh viên
    conn = None
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "UPDATE grades SET score = %s WHERE student_id = %s AND subject_id = %s"
        for g in listGrade:
            cursor.execute(sql, (g.score, g.student_id, g.subject_id))
        conn.commit()
        cursor.close()
        return True
    except Exception as ex:
        print(ex)
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()

def deleteGrade(student_id, subject_id):  # xóa điểm của 1 sinh viên
    conn = None
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "DELETE FROM grades WHERE student_id = %s AND subject_id = %s"
        cursor.execute(sql, (student_id, subject_id))
        conn.commit()
        cursor.close()
        return True
    except Exception as ex:
        print(ex)
        if conn:
            conn.rollback()
        return False
    finally:
        if conn:
            conn.close()
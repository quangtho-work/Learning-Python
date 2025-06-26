import dbConnection
from models import subject

def getSubjectList():  # lấy danh sách môn học
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "SELECT subject_id, name FROM subjects"
        cursor.execute(sql)
        subjects = []
        for row in cursor.fetchall():
            subjects.append(subject.Subject(row[1], subject_id=row[0]))
        cursor.close()
        return subjects
    except Exception as e:
        print("Error connecting to the database:", e)
    finally:
        if conn:
            conn.close()
    return None

def getSubjectById(id):  # lấy môn học theo id
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "SELECT subject_id, name FROM subjects WHERE subject_id = %s"
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return subject.Subject(row[1], subject_id=row[0])
        return None
    except Exception as e:
        print("Error connecting to the database:", e)
    finally:
        if conn:
            conn.close()
    return None

def addSubject(subject_obj: subject.Subject):  # thêm môn học
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "INSERT INTO subjects (name) VALUES (%s)"
        cursor.execute(sql, (subject_obj.name,))
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

def updateSubject(subject_obj: subject.Subject):  # cập nhật môn học
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "UPDATE subjects SET name = %s WHERE subject_id = %s"
        cursor.execute(sql, (subject_obj.name, subject_obj.subject_id))
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

def deleteSubject(id: int):  # xóa môn học
    try:
        conn = dbConnection.getConnection()
        cursor = conn.cursor()
        sql = "DELETE FROM subjects WHERE subject_id = %s"
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
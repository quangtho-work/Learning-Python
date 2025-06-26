import psycopg2

def getConnection():
    try:
        conn = psycopg2.connect(
            dbname="student_management",
            user="postgres",
            password="132003",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        return None
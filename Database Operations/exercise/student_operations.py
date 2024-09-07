import psycopg2

def addStudents(connection):
    # Open a cursor to perform database operations
    cursor = connection.cursor()
    
    try:
        # Execute insert
        insertQuery = "insert into student values (%d, '%s', %d);"
        cursor.execute(insertQuery % (1, "Lucia", 50))
        cursor.execute(insertQuery % (2, "Sasha", 51))
        connection.commit()
        print("Students added")
    finally:
        cursor.close()

def readStudents(connection):
    # Open a cursor to perform database operations
    cursor = connection.cursor()
    
    try:
        # Execute select
        cursor.execute("select * from student;")
        rows = cursor.fetchall()
        print("Total number of records", cursor.rowcount)
        for row in rows:
            print(row)
    finally:
        cursor.close()
    
    
def updateStudent(connection, studentId, age):
    # Open a cursor to perform database operations
    cursor = connection.cursor()
    
    try:
        # Execute insert
        updateQuery = "update student set age = %d where student_id = %d;"
        cursor.execute(updateQuery % (age, studentId))
        connection.commit()
        print("Student updated")
    finally:
        cursor.close()

def deleteStudent(connection, studentId):
    # Open a cursor to perform database operations
    cursor = connection.cursor()
    
    try:
        # Execute insert
        updateQuery = "delete from student where student_id = %d;"
        cursor.execute(updateQuery % (studentId))
        connection.commit()
        print("Student deleted")
    finally:
        cursor.close()
# Connect to an existing database
connection = psycopg2.connect("dbname=python_test user=python_test password=python_test")
try:
    addStudents(connection)
    readStudents(connection)
    updateStudent(connection, 2, 52)
    readStudents(connection)
    deleteStudent(connection, 2)
    readStudents(connection)
except Exception as e:
    connection.rollback()
    print("Error", e)    
finally:
    connection.close()

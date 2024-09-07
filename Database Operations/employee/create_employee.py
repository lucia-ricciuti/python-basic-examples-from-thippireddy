import psycopg2

# Connect to an existing database
connection = psycopg2.connect("dbname=python_test user=python_test password=python_test")

# Open a cursor to perform database operations
cursor = connection.cursor()

try:
    # Execute a command
    cursor.execute("insert into employee values ('3', 'Vasil', 5500);")
    connection.commit()
    print("Employee added")
except:
    connection.rollback()    
finally:
    cursor.close()
    connection.close()
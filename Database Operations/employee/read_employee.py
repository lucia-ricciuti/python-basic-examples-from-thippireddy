import psycopg2

# Connect to an existing database
connection = psycopg2.connect("dbname=python_test user=python_test password=python_test")

# Open a cursor to perform database operations
cursor = connection.cursor()

# Execute a command
cursor.execute("select * from employee;")
"""
row = cursor.fetchone()
while row is not None:
    print(row)    
    row = cursor.fetchone()
    """
rows = cursor.fetchall()
print("Total number of records", cursor.rowcount)
for row in rows:
    print(row)
    
cursor.close()
connection.close()
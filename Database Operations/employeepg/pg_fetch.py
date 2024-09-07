import psycopg2

connection = psycopg2.connect(database="employeedb",
                              user="test",
                              password="password",
                              host="127.0.0.1",
                              port="5432")

print("Connected to EmployeeDB")
cursor = connection.cursor()
cursor.execute("select * from employee")
rows = cursor.fetchall()
print("Employee fetch")
for row in rows:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Sal:", row[2])

connection.close()